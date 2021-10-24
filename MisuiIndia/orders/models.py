from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from products_api.models import ProductModel,SellerProductModel
from authentication.models import CustomUser

class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  blank = False)
    product = models.ForeignKey(SellerProductModel, on_delete=models.CASCADE, blank = False)
    # amount = models.IntegerField(default=1, blank = False)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    deliveryaddress = models.CharField(max_length =100, blank = False)
    pickupaddress = models.CharField(max_length =100, blank = False)
    orederTime = models.DateTimeField(auto_now=True, null=True)
    deliverydescription = models.CharField(max_length = 100, null =True, blank = True)
    def __str__(self):
        return str(self.user) + ' ordered ' + str(self.product)


