from django.contrib import admin

from ..models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''Admin View for Cart'''

    list_display = ('user',)
    filter_horizontal = ('items',)
