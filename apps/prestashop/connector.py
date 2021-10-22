from urllib.parse import urlencode
import requests

from django.conf import settings

from apps.prestashop.models import PrestashopSynchronizer as PrestaSync
from apps.products.models import Product


class PsProductConnector:
    """
    Mange product prestashop
    """
    URL_BASE = settings.PRESTASHOP_URL_BASE + 'products/'
    PRESTASHOP_TOKEN = settings.PRESTASHOP_TOKEN

    def __init__(self):
        self.request = requests.Session()
        self.request.auth = (self.PRESTASHOP_TOKEN, '')
        self.request.headers = {"Output-Format": "JSON"}

    def _get(self, url):
        try:
            return self.request.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            raise

    def _products(self):
        url = self.URL_BASE
        return self._get(url)

    def _product(self, ps_id):
        url = self.URL_BASE + "" + str(ps_id)
        return self._get(url)

    def products(self, ps_id=None):
        if not ps_id:
            return self._products().json()['products']
        return self._product(ps_id).json()['product']


def update_product(product):
    return f"update product {product['id']}"


def save_product_sync(product):
    prestashop_sync = PrestaSync.objects.filter(entity_type=PrestaSync.ENTITY_TYPE_PRODUCT,
                                                prestashop_entity_id=product["id"])

    if not prestashop_sync:
        PrestaSync.objects.create(entity_type=PrestaSync.ENTITY_TYPE_PRODUCT,
                                  prestashop_entity_id=product["id"],
                                  raw_data=product
                                  )
    else:
        update_product(product)
