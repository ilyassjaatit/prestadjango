from django.contrib import admin
from .models import Product, Tag, Category, ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Category)
