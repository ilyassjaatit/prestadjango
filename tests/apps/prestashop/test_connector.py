import pytest
from apps.products.models import Product
from apps.prestashop.models import PrestashopSynchronizer as PrestaSync
from apps.prestashop.connector import save_product, update_product

pytestmark = pytest.mark.django_db


def test_save_product():
    product = {
        "id": 1,
        "name": "product name",
        "reference": '0001'
    }
    save_product(product)
    db_product = Product.objects.get(sku=product['reference'],
                                     name=product['name'])

    prest_sync = PrestaSync.objects.get(prestashop_entity_id=product['id'],
                                        entity_id=db_product.pk,
                                        entity_type=PrestaSync.PRODUCT)
    assert prest_sync is not None
    assert db_product.name == product['name']

def test_update_product():
    product = {
        "id": 1,
        "name": "product name",
        "reference": '0001'
    }
    assert update_product(product) == f"update product {product['id']}"