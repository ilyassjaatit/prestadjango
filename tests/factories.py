import factory
from faker import Faker
from apps.products.models import Product

fake = Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Product name ????-########")

    class Meta:
        model = Product
