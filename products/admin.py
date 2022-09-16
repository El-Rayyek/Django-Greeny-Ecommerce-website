from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product , Category , Brand , Review , ProductImage

#Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImageInline]
    summernote_fields = '__all__'


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImage)