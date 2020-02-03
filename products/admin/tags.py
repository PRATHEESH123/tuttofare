from django.contrib import admin

# local
from ..models import Tag



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    '''Admin View for Tag'''

    list_display = ('name',)
    filter_horizontal = ('products',)
