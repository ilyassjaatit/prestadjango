import pytest
from pytest_factoryboy import register
from tests.factories import ProductFactory, UserFactory

# Register factories to pytest global namespace.
register(UserFactory)
register(ProductFactory)


@pytest.fixture
def create_products(db, product_factory):
    def _create_products(size=10):
        return product_factory.simple_generate_batch(create=True, size=size)

    return _create_products
