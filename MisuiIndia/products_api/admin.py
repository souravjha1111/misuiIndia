from django.contrib import admin
from .models import ProductModel
# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    model = ProductModel

admin.site.register(ProductModel, ProductModelAdmin),