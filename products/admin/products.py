from django.contrib import admin

# MPTT
from mptt.admin import TreeRelatedFieldListFilter

# # tranlations
# from modeltranslation.admin import TranslationAdmin

# summernote (rich text field)
from django_summernote.admin import SummernoteModelAdmin

# local
from ..models import Product, ProductImage, ProductReview, Brand , Tag

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    # verbose_name = 'sub category'
    # verbose_name_plural = 'sub categories'
    show_change_link = True


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'stock', 'average_rating')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
    ] 

class TagInline(admin.TabularInline):
    '''Tabular Inline View for Tag'''

    model = Tag.products.through
    verbose_name= 'Tag'
    verbose_name_plural= 'Tags'
    extra = 0 


