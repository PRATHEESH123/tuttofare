# django rest framework
from rest_framework import serializers

# local
from ..models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
            'alt',
        )

    def to_representation(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    rating = serializers.IntegerField(default=10)  # should start from 10
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'rating',
            'stock',
            'category',
            'images',
        )
