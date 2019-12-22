# 3rd party
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

# local
from .models import Category, Product, ProductImage, ProductReview


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


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
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
            'no_of_stars',
            'posted_on',
        )