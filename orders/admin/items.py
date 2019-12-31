from django.contrib import admin

# local
from ..models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    '''Admin View for Item'''
