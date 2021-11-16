import pytest

from apps.products.models import ProductContent
from tests.factories import (
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    TagFactory,
)

pytestmark = pytest.mark.django_db

NUM_OF_ITEMS = 10


def test_create_product():
    name = "Product name 1"
    product = ProductFactory(name=name)
    assert product.name == name


def test_create_product_image():
    name = "Product image name 1"
    image = ProductImageFactory(name=name)
    assert name == image.name


def test_create_product_content(create_products_content):
    create_products_content(NUM_OF_ITEMS)
    assert ProductContent.objects.count() == NUM_OF_ITEMS


def test_create_tag(create_products):
    name = "Tag name 1"
    tag = TagFactory(name=name)
    assert tag.name == name


def test_create_category(create_products):
    name = "Category name 1"
    product = CategoryFactory(name=name)
    assert product.name == name
