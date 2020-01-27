from django.contrib import admin

# local
from ..models import Brand

# tranlations
from modeltranslation.admin import TranslationAdmin

@admin.register(Brand)
class BrandAdmin(TranslationAdmin):
    '''Admin View for Brand'''

    list_display = ('name',)
    filter_horizontal = ('products',)