from django.contrib import admin

from ..models import CartItem


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    '''Admin View for Cart'''

    list_display = ('user',)
