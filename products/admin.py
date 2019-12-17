from django.contrib import admin

# 3rd party
from mptt.admin import DraggableMPTTAdmin

# local
from .models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    '''Admin View for Category'''
    list_display = (
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    )
    list_display_links = ('indented_title',)