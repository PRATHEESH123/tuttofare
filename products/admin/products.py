from django.contrib import admin

# MPTT
from mptt.admin import TreeRelatedFieldListFilter

# tranlations
from modeltranslation.admin import TranslationAdmin

# summernote (rich text field)
from django_summernote.admin import SummernoteModelAdmin

# local
from ..models import Product, ProductImage, ProductReview, Brand


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


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin, TranslationAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'stock', 'average_rating')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
        BrandInline,
    ]
    summernote_fields = ('descrption',)
