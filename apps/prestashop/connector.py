from abc import ABC

from django.conf import settings
from django.db import Error as django_error

import requests

from apps.customers.models import Customer
from apps.prestashop.models import PrestashopSynchronizer as PrestaSync

from .config import (
    RESOURCES_TYPE_ADDRESSES,
    RESOURCES_TYPE_CARTS,
    RESOURCES_TYPE_CATEGORIES,
    RESOURCES_TYPE_COSTUMERS,
    RESOURCES_TYPE_COUNTRIES,
    RESOURCES_TYPE_ORDER_DETAILS,
    RESOURCES_TYPE_ORDERS,
    RESOURCES_TYPE_PRODUCTS,
    RESOURCES_TYPE_TAGS,
    RESOURCES_TYPE_ZONES,
    STATUS_CREATED,
    STATUS_NOT_CREATED,
)


class PsConnector:
    _URL_BASE = settings.PRESTASHOP_URL_BASE
    PRESTASHOP_TOKEN = settings.PRESTASHOP_TOKEN

    def __init__(self):
        self.request = requests.Session()
        self.request.auth = (self.PRESTASHOP_TOKEN, "")
        self.request.headers = {"Output-Format": "JSON"}
        self.sync_model = PrestaSync
        self.items = []

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
    RESOURCES_TYPE: str
    singular_name: str

    def __init__(self):
        super().__init__()
        self.resources_name = self.RESOURCES_TYPE.lower()

    def _url(self, resources_id=None):
        url = str(self.url_base()) + str(self.resources_name) + "/"
        if resources_id:
            return url + str(resources_id) + "/"
        return url

    def url(self, id_resource=None):
        return self._url(id_resource)

    # TODO Use generator in the next iteration
    def _resources(self):
        response = self.get(self.url()).json()
        data_row = response[self.resources_name]
        if data_row:
            for item in data_row:
                self.items.append(item)
        return self.items

    def _resource(self, id_resource):
        response = self.get(self.url(id_resource)).json()
        return response[self.singular_name]

    def resources(self, id_resource=None):
        if id_resource:
            return self._resource(id_resource)
        return self._resources()

    def _exist_resource(self, id_resources):
        return self.sync_model.objects.filter(
            resources_type=self.RESOURCES_TYPE, prestashop_entity_id=id_resources
        )

    def save_resources(self):
        for item in self.items:
            if not self._exist_resource(item["id"]):
                data = self.resources(item["id"])
                self.sync_model.objects.create(
                    prestashop_entity_id=item["id"],
                    resources_type=self.RESOURCES_TYPE,
                    raw_data=data,
                )


class PsProduct(PsGetResources):
    """
    Mange product prestashop
    """

    RESOURCES_TYPE = RESOURCES_TYPE_PRODUCTS
    singular_name = "product"


class PsCustomers(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_COSTUMERS
    singular_name = "customer"
    limit = 1000

    def __init__(self):
        super().__init__()
        self.model = Customer

    @staticmethod
    def save_customers():
        """
        Save in django entity
        :return: True
        """

        ps_customers = PrestaSync.objects.filter(
            status=STATUS_NOT_CREATED, entity_type=RESOURCES_TYPE_COSTUMERS
        )
        for ps in ps_customers:
            raw_data = ps.raw_data
            customer = Customer(
                last_name=raw_data["lastname"],
                first_name=raw_data["firstname"],
                email=raw_data["email"],
                active=raw_data["active"],
                created_at=raw_data["date_add"],
            )
            try:
                customer.save()
                print(customer.email)
            except django_error:
                print(raw_data["email"])

            if customer.pk:
                PrestaSync.objects.filter(pk=ps.pk).update(
                    status=STATUS_CREATED, entity_id=customer.pk
                )


class PsCards(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_CARTS
    singular_name = "cart"
    limit = 3000


class PsOrders(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_ORDERS
    singular_name = "order"


class PsOrderDetails(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_ORDER_DETAILS
    singular_name = "order_detail"


class PsAddresses(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_ADDRESSES
    singular_name = "address"
    limit = 1000


class PsZones(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_ZONES
    singular_name = "zone"


class PsCountry(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_COUNTRIES
    singular_name = "country"


class PsCategories(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_CATEGORIES
    singular_name = "category"


class PsTags(PsGetResources):
    RESOURCES_TYPE = RESOURCES_TYPE_TAGS
    singular_name = "tag"
