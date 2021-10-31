import pytest
from pytest_factoryboy import register
from tests.factories import \
    ProductFactory, \
    CategoryFactory, \
    TagFactory, \
    UserFactory, \
    CustomerFactory, \
    OrderFactory

# Register factories to pytest global namespace.
register(UserFactory)
register(ProductFactory)
register(TagFactory)
register(CategoryFactory)
register(CustomerFactory)
register(OrderFactory)


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
def create_customers(db, customer_factory):
    def _create_customers(size=10):
        return customer_factory.simple_generate_batch(create=True, size=size)

    return _create_customers


@pytest.fixture
def create_orders(db, order_factory):
    def _create_orders(size=10):
        return order_factory.simple_generate_batch(create=True, size=size)

    return _create_orders

@pytest.fixture
def create_tags(db, tag_factory):
    def _create_tags(size=10):
        return tag_factory.simple_generate_batch(create=True, size=size)

    return _create_tags

@pytest.fixture
def create_categories(db, category_factory):
    def _create_categories(size=10):
        return category_factory.simple_generate_batch(create=True, size=size)

    return _create_categories
