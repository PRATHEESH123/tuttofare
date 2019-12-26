# 3rd party
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

# local
from .models import Category, Product, ProductImage, ProductReview, Collection, CollectionImage


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, allow_null=True, many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'cover',
            'parent',
            'children',
        )


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
            'in_stock',
            'category',
            'images',
        )


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = ProductReview
        fields = (
            'id',
            'user',
            'product',
            'text',
            'rating',
            'posted_on',
        )


class CollectionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectionImage
        fields = (
            'id',
            'image',
            'alt',
        )

    def to_representation(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class CollectionsSerializer(serializers.ModelSerializer):
    images = CollectionImageSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Collection
        fields = (
            'id',
            'name',
            'products',
            'images',
        )
