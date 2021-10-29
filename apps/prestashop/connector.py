from abc import ABC
import requests

from django.conf import settings

from apps.prestashop.models import PrestashopSynchronizer as PrestaSync
from apps.customers.models import Customer
from .config import *


class PsConnector:
    _URL_BASE = settings.PRESTASHOP_URL_BASE
    PRESTASHOP_TOKEN = settings.PRESTASHOP_TOKEN

    def __init__(self):
        self.request = requests.Session()
        self.request.auth = (self.PRESTASHOP_TOKEN, '')
        self.request.headers = {"Output-Format": "JSON"}
        self.sync_model = PrestaSync
        self.items = None

    def _get(self, url):
        try:
            return self.request.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            raise

    def get(self, url):
        return self._get(url)

    def url_base(self):
        return self._URL_BASE


class PsGetResources(PsConnector, ABC):
    resources_name: str
    singular_name: str

    def _url(self, ps_id=None):
        url = str(self.url_base()) + str(self.resources_name)
        if ps_id:
            return url + "/" + str(ps_id) + "/"
        return url

    def url(self, id_resource=None):
        return self._url(id_resource)

    def _resources(self):
        return self.get(self.url())

    def _resource(self, id_resource):
        print(self.url())
        return self.get(self.url(id_resource))

    def resources(self, id_resource=None):
        if id_resource:
            return self._resource(id_resource).json()[self.singular_name]
        return self._resources().json()[self.resources_name]


class PsProduct(PsGetResources):
    """
    Mange product prestashop
    """
    resources_name = "products"
    singular_name = "product"


class PsCustomers(PsConnector):
    URL_BASE = PsConnector._URL_BASE + 'customers/'

    def __init__(self):
        super().__init__()
        self.model = Customer

    def _customers(self):
        self.items = self._get(self.URL_BASE).json()['customers']
        return self.items

    def _customer(self, ps_id):
        url = self.URL_BASE + "" + str(ps_id)
        return self._get(url)

    def customers(self, ps_id=None):
        if not ps_id:
            return self._customers()
        return self._customer(ps_id).json()['customer']

    def _exist_item(self, id):
        return self.sync_model \
            .objects \
            .filter(entity_type=PrestaSync.ENTITY_TYPE_COSTUMER,
                    prestashop_entity_id=id)

    def save_items(self):
        if not self.items:
            self._customers()
        for item in self.items:
            if not self._exist_item(item['id']):
                data = self.customers(item['id'])
                self.sync_model.objects.create(
                    prestashop_entity_id=item['id'],
                    entity_type=PrestaSync.ENTITY_TYPE_COSTUMER,
                    raw_data=data
                )
            else:
                print(item)

    @staticmethod
    def save_customers():
        """
        Save in django entity
        :return: True
        """

        ps_customers = PrestaSync. \
            objects. \
            filter(status=PrestaSync.STATUS_NOT_CREATED,
                   entity_type=PrestaSync.ENTITY_TYPE_COSTUMER
                   )
        for ps in ps_customers:
            raw_data = ps.raw_data
            customer = Customer(
                last_name=raw_data['lastname'],
                first_name=raw_data['firstname'],
                email=raw_data['email'],
                active=raw_data['active'],
                created_at=raw_data['date_add'],
            )
            try:
                customer.save()
            except:
                print(raw_data)
                break

            if customer.pk:
                PrestaSync.objects.filter(pk=ps.pk).update(status=PrestaSync.STATUS_CREATED, entity_id=customer.pk)


class PsOrders(PsGetResources):
    resources_name = 'orders'
    singular_name = 'order'

    def _exist_item(self, id):
        return self.sync_model \
            .objects \
            .filter(entity_type=PrestaSync.ENTITY_TYPE_ORDERS,
                    prestashop_entity_id=id)

    def save_items(self):
        if not self.items:
            self.items = self.resources()
        for item in self.items:
            if not self._exist_item(item['id']):
                data = self.resources(item['id'])
                import time
                time.sleep(.3)
                self.sync_model.objects.create(
                    prestashop_entity_id=item['id'],
                    entity_type=PrestaSync.ENTITY_TYPE_ORDERS,
                    raw_data=data
                )
            else:
                print(item)


def update_product(product):
    return f"update product {product['id']}"


def save_product_sync(product):
    prestashop_sync = PrestaSync.objects.filter(entity_type=RESOURCES_TYPE_PRODUCTS,
                                                prestashop_entity_id=product["id"])

    if not prestashop_sync:
        PrestaSync.objects.create(entity_type=RESOURCES_TYPE_PRODUCTS,
                                  prestashop_entity_id=product["id"],
                                  raw_data=product
                                  )
    else:
        update_product(product)
