from django.contrib import admin

# 3rd party
from mptt.admin import TreeRelatedFieldListFilter

# local
from ..models import Product, ProductImage, ProductReview


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

    list_display = ('name', 'price', 'descrption', 'average_rating')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
    ]
