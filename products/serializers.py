# 3rd party
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

# local
from .models import Category


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
