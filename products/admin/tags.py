from django.contrib import admin

# local
from ..models import Tag

# tranlations
from modeltranslation.admin import TranslationAdmin

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    '''Admin View for Tag'''

    list_display = ('name',)
    filter_horizontal = ('products',)
