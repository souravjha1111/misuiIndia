from django.contrib import admin
from .models import OrderModel
# Register your models here.

class CustomOrderModelAdmin(admin.ModelAdmin):
    model = OrderModel

admin.site.register(OrderModel, CustomOrderModelAdmin)