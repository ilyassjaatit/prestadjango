import pytest

from apps.customers.models import Customer

pytestmark = pytest.mark.django_db

NUMBER_OF_ITEMS = 10


def test_create_create_customers(create_customers):
    create_customers(NUMBER_OF_ITEMS)
    customers_count = Customer.objects.all().count()
    assert customers_count == NUMBER_OF_ITEMS
