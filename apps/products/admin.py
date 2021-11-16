from django.contrib import admin

from .models import Category, Product, ProductContent, ProductImage, Tag

admin.site.register(Product)
admin.site.register(ProductContent)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Category)
