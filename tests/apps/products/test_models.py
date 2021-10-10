import pytest
from tests.factories import ProductFactory, TagFactory, CategoryFactory

pytestmark = pytest.mark.django_db


def test_create_product():
    name = "Product name 1"
    product = ProductFactory(name=name)
    assert product.name == name


def test_create_tag(create_products):
    name = "Tag name 1"
    tag = TagFactory(name=name)
    assert tag.name == name


def test_create_category(create_products):
    name = "Category name 1"
    product = CategoryFactory(name=name)
    assert product.name == name
