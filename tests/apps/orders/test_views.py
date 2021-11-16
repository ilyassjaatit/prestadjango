import json

from django.urls import reverse

from rest_framework import status

from apps.orders.models import Order
from apps.orders.views import OrderViewSet

NUM_OF_PRODUCTS = 30


class TestProductViewSet:
    def test_list(self, rf, create_orders, create_user):
        url = reverse("api:order-list")
        view = OrderViewSet.as_view({"get": "list"})
        request = rf.get(url)
        request.user = create_user
        create_orders(NUM_OF_PRODUCTS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)["count"] == NUM_OF_PRODUCTS

    def test_retrieve(self, rf, create_orders, create_user):
        create_orders()
        order = Order.objects.first()
        url = reverse("api:order-detail", kwargs={"pk": order.id})
        view = OrderViewSet.as_view({"get": "retrieve"})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=order.pk).render()
        assert status.HTTP_200_OK == response.status_code
