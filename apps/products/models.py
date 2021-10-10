from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, help_text=_("Product name"))
    sku = models.CharField(max_length=80, help_text=_("Stock keeping unit"))

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, help_text=_("Tag name"))
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, help_text=_("Category name"))
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name
