from urllib.parse import urlencode
import requests

from django.conf import settings

from apps.prestashop.models import PrestashopSynchronizer as PrestaSync
from apps.products.models import Product


def update_product(product):
    return f"update product {product['id']}"


def save_product(product):
    prestashop_sync = PrestaSync.objects.filter(entity_type=PrestaSync.PRODUCT,
                                                 prestashop_entity_id=product["id"])

    if not prestashop_sync:
        PrestaSync.objects.create(entity_type=PrestaSync.PRODUCT,
                                  prestashop_entity_id=product["id"],
                                  raw_data=product
                                  )
    else:
        update_product(product)


def get_products(product_id=None):
    url_products_base = settings.PRESTASHOP_URL_BASE + 'products/'
    if not product_id:
        url = url_products_base + '?' + urlencode({"output_format": "JSON"})
        req = requests.get(url, auth=(settings.PRESTASHOP_TOKEN, ''))
    else:
        url = url_products_base + str(product_id) + '/?' + urlencode({"output_format": "JSON"})
        req = requests.get(url, auth=(settings.PRESTASHOP_TOKEN, ''))
    return req.json()
