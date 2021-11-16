import pytest

from apps.orders.models import Order

pytestmark = pytest.mark.django_db

NUMBER_OF_ITEMS = 10


def test_create_order(create_orders):
    create_orders(NUMBER_OF_ITEMS)
    assert Order.objects.count() == NUMBER_OF_ITEMS


def test_create_order_item(create_order_items):
    create_order_items(NUMBER_OF_ITEMS)
    assert Order.objects.count() == NUMBER_OF_ITEMS
