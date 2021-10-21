import pytest
import json

from django.urls import reverse
from apps.products.models import Product
from apps.products.views import ProductViewSet
from rest_framework import status
from tests.factories import UserFactory

NUM_OF_PRODUCTS = 30


@pytest.fixture()
def create_user():
    user = UserFactory(username="name")
    yield user


class TestProductViewSet:

    def test_list(self, rf, create_products, create_user):
        url = reverse('api:product-list')
        view = ProductViewSet.as_view(
            {'get': 'list'}
        )
        request = rf.get(url)
        request.user = create_user
        create_products(NUM_OF_PRODUCTS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)['count'] == NUM_OF_PRODUCTS

    def test_retrieve(self, rf, create_products, create_user):
        create_products()
        product = Product.objects.first()
        url = reverse('api:product-detail', kwargs={'pk': product.id})
        view = ProductViewSet.as_view({'get': 'retrieve'})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=product.pk).render()
        assert status.HTTP_200_OK == response.status_code
