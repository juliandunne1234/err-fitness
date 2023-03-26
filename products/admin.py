from django.contrib import admin
from .models import Product, Category, Review
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ReviewAdmin(SummernoteModelAdmin):

    list_display = (
        'product',
        'review_by',
        'rating'
    )
    summernote_fields = ('comment')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
