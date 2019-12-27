from django.contrib import admin

from ..models import Cart, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''Admin View for Cart'''

    list_display = ('user',)
    inlines = [
        ItemInline,
    ]