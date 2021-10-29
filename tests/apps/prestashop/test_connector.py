import pytest
from apps.prestashop.models import PrestashopSynchronizer as PrestaSync
from apps.prestashop.connector import save_product_sync, update_product
from apps.prestashop.config import RESOURCES_TYPE_PRODUCTS

pytestmark = pytest.mark.django_db


def test_save_product_sync():
    product = {
        'id': 99999999,
        "reference": "ref 123",
        'name': [
            {'id': '1', 'value': 'product name'}
        ]
    }
    product_name = product['name'][0]['value']

    save_product_sync(product)

    prest_sync = PrestaSync.objects.get(prestashop_entity_id=product['id'],
                                        entity_type=RESOURCES_TYPE_PRODUCTS,
                                        raw_data=product
                                        )
    assert prest_sync is not None
    assert prest_sync.__str__() == RESOURCES_TYPE_PRODUCTS + " " + product_name


def test_update_product():
    product = {
        "id": 1,
        "name": "product name",
        "reference": '0001'
    }
    assert update_product(product) == f"update product {product['id']}"
