from django.contrib import admin
from .models import Category, Brand, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "brand", "category", "price", "created_on"]
    list_filter = ["brand", "category", "created_on"]
    search_fields = [
        "title",
        "brand__name",
    ]

    ordering = ["-created_on"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]


admin.site.register(Category)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
