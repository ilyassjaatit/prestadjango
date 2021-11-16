import pytest
import json

from django.urls import reverse
from apps.products.models import Product, Category, Tag
from apps.products.views import ProductViewSet, CategoryViewSet, TagViewSet
from rest_framework import status

NUM_OF_ITEMS = 30


class TestProductViewSet:
    def test_list(self, rf, create_products, create_user):
        url = reverse("api:product-list")
        view = ProductViewSet.as_view({"get": "list"})
        request = rf.get(url)
        request.user = create_user
        create_products(NUM_OF_ITEMS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)["count"] == NUM_OF_ITEMS

    def test_retrieve(self, rf, create_products, create_user):
        create_products()
        product = Product.objects.first()
        url = reverse("api:product-detail", kwargs={"pk": product.id})
        view = ProductViewSet.as_view({"get": "retrieve"})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=product.pk).render()
        assert status.HTTP_200_OK == response.status_code


class TestCategoryViewSet:
    def test_list(self, rf, create_categories, create_user):
        url = reverse("api:category-list")
        view = CategoryViewSet.as_view({"get": "list"})
        request = rf.get(url)
        request.user = create_user
        create_categories(NUM_OF_ITEMS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)["count"] == NUM_OF_ITEMS

    def test_retrieve(self, rf, create_categories, create_user):
        create_categories()
        category = Category.objects.first()
        url = reverse("api:category-detail", kwargs={"pk": category.id})
        view = CategoryViewSet.as_view({"get": "retrieve"})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=category.pk).render()
        assert status.HTTP_200_OK == response.status_code


class TestTagViewSet:
    def test_list(self, rf, create_tags, create_user):
        url = reverse("api:tag-list")
        view = TagViewSet.as_view({"get": "list"})
        request = rf.get(url)
        request.user = create_user
        create_tags(NUM_OF_ITEMS)
        response = view(request).render()
        assert status.HTTP_200_OK == response.status_code
        assert json.loads(response.content)["count"] == NUM_OF_ITEMS

    def test_retrieve(self, rf, create_tags, create_user):
        create_tags()
        tag = Tag.objects.first()
        url = reverse("api:tag-detail", kwargs={"pk": tag.id})
        view = TagViewSet.as_view({"get": "retrieve"})
        request = rf.get(url)
        request.user = create_user
        response = view(request, pk=tag.pk).render()
        assert status.HTTP_200_OK == response.status_code
