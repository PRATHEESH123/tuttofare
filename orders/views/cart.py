# django
from django.shortcuts import get_object_or_404

# django rest framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Cart
from ..serializers import CartItemAddSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Cart.objects.filter(user=self.request.user)
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            return CartItemAddSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data[0]['items'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def decrement(self, request, pk):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        item.quantity -= 1 if item.quantity > 1 else 0
        item.save()
        return Response(self.get_serializer(item).data)