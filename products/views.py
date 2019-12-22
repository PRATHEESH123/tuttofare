# 3rd party
from rest_framework import viewsets, mixins

from django_filters.rest_framework import DjangoFilterBackend

# local
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']