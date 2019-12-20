# 3rd party
from rest_framework import viewsets, mixins

# local
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer