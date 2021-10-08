import pytest
from tests.factories import ProductFactory

pytestmark = pytest.mark.django_db
def test_create_product():
    name = "product name 1"
    product = ProductFactory(name=name)
    assert product.name == name