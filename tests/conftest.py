import pytest
from pytest_factoryboy import register
from tests.factories import ProductFactory, UserFactory, CustomerFactory

# Register factories to pytest global namespace.
register(UserFactory)
register(ProductFactory)
register(CustomerFactory)


@pytest.fixture()
def create_user():
    user = UserFactory(username="name")
    yield user


@pytest.fixture
def create_products(db, product_factory):
    def _create_products(size=10):
        return product_factory.simple_generate_batch(create=True, size=size)

    return _create_products


@pytest.fixture
def create_customer(db, customer_factory):
    def _create_customer(size=10):
        return customer_factory.simple_generate_batch(create=True, size=size)

    return _create_customer
