from rest_framework import serializers

from .models import Category, Product, ProductContent, ProductImage, Tag


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    image_default = serializers.SerializerMethodField()

    def get_content(self, obj):
        try:
            data_serializers = ProductContentSerializer(obj.productcontent)
            return data_serializers.data
        except:
            return {}

    def get_image_default(self, obj):
        try:
            image = ProductImage.objects.get(product__pk=obj.pk, default=True)
            data_serializers = ProductImageSerializer(image)
            return data_serializers.data
        except:
            return {}

    class Meta:
        model = Product
        fields = ["id", "name", "sku", "content", "image_default"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
