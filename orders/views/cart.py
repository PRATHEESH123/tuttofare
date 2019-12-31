# django
from django.shortcuts import get_object_or_404

# django rest framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Item
from ..serializers import ItemSerializer, ItemCreateSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Item.objects.filter(cart__user=self.request.user)
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        return super().get_serializer_class()

    @action(detail=True)
    def decrement(self, request, pk):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        item.quantity -= 1 if item.quantity > 1 else 0
        item.save()
        return Response(self.get_serializer(item).data)