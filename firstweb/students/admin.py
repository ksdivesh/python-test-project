from django.contrib import admin
from students.models import Category, Product, ProductImage, SliderImage
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(SliderImage)

# admin.site.register(ProductImage)
