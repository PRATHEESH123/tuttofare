# django rest framework
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# local
from products.serializers import ProductSerializer
from products.models import Product


class WishlistProductsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(wishlist__user=user)

    @action(detail=True)
    def add(self, request, pk=None):
        user = self.request.user
        user.wishlist.products.add(pk)
        return Response('products added')

    @action(detail=True)
    def remove(self, request, pk=None):
        user = self.request.user
        user.wishlist.products.remove(pk)
        return Response('products removed')