import json

from django.urls import reverse
from apps.customers.models import Customer
from apps.customers.views import CustomerViewSet
from rest_framework import status

NUM_OF_PRODUCTS = 30


class TestProductViewSet:
    def test_list(self, rf, create_customers, create_user):
        url = reverse("api:customer-list")
        view = CustomerViewSet.as_view({"get": "list"})
        request = rf.get(url)
        request.user = create_user
        create_customers(NUM_OF_PRODUCTS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)["count"] == NUM_OF_PRODUCTS

    def test_retrieve(self, rf, create_customers, create_user):
        create_customers()
        customer = Customer.objects.first()
        url = reverse("api:customer-detail", kwargs={"pk": customer.id})
        view = CustomerViewSet.as_view({"get": "retrieve"})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=customer.pk).render()
        assert status.HTTP_200_OK == response.status_code
