from django.db import models
from django.db.models.fields import CharField
from authentication.models import CustomUser

class ProductModel(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images')
    productName = models.CharField(max_length=200)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # image = models.URLField(max_length = 200)   
    brand = models.CharField(max_length=200)
    category =models.CharField(max_length=25, default = 'others')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField()
    rating = models.DecimalField(default = 0,max_digits=2, decimal_places=1, blank = True, null = True)
    numReviews = models.IntegerField(default = 0, blank = True, null = True)
    weight = models.CharField(max_length =20,blank = True,  null = True)
    volume = models.CharField(max_length =20,blank = True,  null = True)
    size = models.CharField(max_length =20, blank = True, null = True)
    color = models.CharField(max_length =20, blank = True, null = True)
    description = models.TextField(max_length =2000, blank = True, null = True)


    def __str__(self):
        return self.productName + ' by ' + str(self.seller)
