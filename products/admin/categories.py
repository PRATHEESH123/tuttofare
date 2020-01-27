from django.contrib import admin

# 3rd party
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline
# local
from ..models import Category


class SubCategoryInline(TranslationTabularInline):
    model = Category
    extra = 0
    verbose_name = 'sub category'
    verbose_name_plural = 'sub categories'
    can_delete = False


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, TranslationAdmin):
    '''Admin View for Category'''
    list_display = (
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    )
    list_display_links = ('indented_title',)
    inlines = [SubCategoryInline]
