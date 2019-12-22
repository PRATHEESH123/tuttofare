# 3rd party
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter

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
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ['category']
    search_fields = ['name']