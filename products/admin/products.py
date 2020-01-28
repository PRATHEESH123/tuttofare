from django.contrib import admin

# MPTT
from mptt.admin import TreeRelatedFieldListFilter

# tranlations
from modeltranslation.admin import TranslationAdmin

# summernote (rich text field)
from django_summernote.admin import SummernoteModelAdmin

# local
from ..models import Product, ProductImage, ProductReview, Brand , Tag


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1


class BrandInline(admin.TabularInline):
    '''Tabular Inline View for Brand'''

    model = Brand.products.through
    verbose_name = 'Brand'
    verbose_name_plural = 'Brands'
    extra = 0

class TagInline(admin.TabularInline):
    '''Tabular Inline View for Tag'''

    model = Tag.products.through
    verbose_name= 'Tag'
    verbose_name_plural= 'Tags'
    extra = 0 

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin, TranslationAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'stock', 'average_rating')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
        BrandInline,
        TagInline,
    ]
    summernote_fields = ('descrption',)
