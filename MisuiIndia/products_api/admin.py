from django.contrib import admin
from .models import ProductModel, SellerProductModel
# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    model = ProductModel


class SellerProductModelAdmin(admin.ModelAdmin):
    model = SellerProductModel

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(SellerProductModel, SellerProductModelAdmin)
