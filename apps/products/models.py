from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, help_text=_("Product name"))
    sku = models.CharField(max_length=80, help_text=_("Stock keeping unit"))
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class ProductContent(models.Model):
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Meta title"),
    )
    meta_description = models.CharField(
        max_length=255, blank=True, null=True, help_text=_("Meta description")
    )
    title = models.CharField(max_length=255, blank=True, null=True, help_text=_("Title "))
    short_description = models.CharField(
        max_length=455, blank=True, null=True, help_text=_("Short description")
    )
    description = models.TextField(blank=True, null=True, help_text=_("Description"))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/")
    default = models.BooleanField(default=False)


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
