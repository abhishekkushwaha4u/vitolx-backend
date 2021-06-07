from rest_framework import serializers
from product.models import (
    Product,
    ProductImage
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductReadOnlySerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.full_name', read_only=True)
    owner_email = serializers.CharField(source='owner.email', read_only=True)
    images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        exclude = ["owner"]
    def get_images(self, obj):
        return ProductImageReadSerializer(ProductImage.objects.filter(product=obj), many=True).data
    

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["owner"]

class ProductImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
