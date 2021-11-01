from datetime import datetime
from django.contrib.auth import get_user_model
import factory
from faker import Faker
from apps.customers.models import Customer
from apps.orders.models import Order
from apps.products.models import Product, ProductImage, Category, Tag, ProductContent
from apps.prestashop.models import PrestashopSynchronizer

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("name")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = (
            extracted
            if extracted
            else factory.Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class CustomerFactory(factory.django.DjangoModelFactory):
    first_name = fake.bothify("first_name ????-########")
    last_name = fake.bothify("last_name ????-########")
    email = factory.LazyAttributeSequence(lambda o, n: '%s@s%d.example.com' % (o, n))
    created_at = '2021-09-19 15:50:44'

    class Meta:
        model = Customer


class ProductFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Product name ????-########")
    created_at = datetime.now()

    class Meta:
        model = Product


class ProductContentFactory(factory.django.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = ProductContent


class ProductImageFactory(factory.django.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = ProductImage


class TagFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Tag name ????-########")
    products = factory.SubFactory(ProductFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.products.add(extracted)

    class Meta:
        model = Tag


class CategoryFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Category name ????-########")
    products = factory.SubFactory(ProductFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.products.add(extracted)

    class Meta:
        model = Category


class PrestashopSynchronizerFactory(factory.django.DjangoModelFactory):
    entity_id = 1
    prestashop_entity_id = 1
    raw_data = {
        'id': 99999999,
        'name': [
            {'id': '1', 'value': 'product name'}
        ]
    }

    class Meta:
        model = PrestashopSynchronizer


class OrderFactory(factory.django.DjangoModelFactory):
    customer = factory.SubFactory(CustomerFactory)
    created_at = datetime.now()

    class Meta:
        model = Order
