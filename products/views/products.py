# 3rd party
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter

# django filter
from django_filters.rest_framework import DjangoFilterBackend

# local
from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ['category']
    search_fields = ['name']
