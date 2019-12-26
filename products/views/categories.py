# 3rd party
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# local
from ..models import Category
from ..serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
