from django.contrib import admin

# tranlations
from modeltranslation.admin import TranslationAdmin

# local
from ..models import Collection, CollectionImage


class ImageInline(admin.TabularInline):
    model = CollectionImage
    extra = 1


@admin.register(Collection)
class CollectionAdmin(TranslationAdmin):
    '''Admin View for Collection'''

    list_display = ('name',)
    filter_horizontal = ('products',)
    inlines = [
        ImageInline,
    ]