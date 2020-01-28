# django rest framework
from rest_framework import serializers

# djangorestframework-recursive
from rest_framework_recursive.fields import RecursiveField

# local
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, allow_null=True, many=True)
    no_of_product = serializers.IntegerField(source='product_set.count')

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'cover',
            'parent',
            'children',
            'no_of_product',
        )