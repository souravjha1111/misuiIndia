from django.db import models
from django.db.models.fields import CharField
from authentication.models import CustomUser
import time
from django.contrib.postgres.fields import JSONField

class ProductModel(models.Model):
    category_choice = (('electronics', 'electronics'),    ('vegetable', 'vegetable'),        ('cloth', 'cloth'),  ('fruits', 'fruits'),('furniture', 'Female'),  ('book', 'book'),        ('others', 'others'))
    img = models.ImageField(null=True, blank=True, upload_to = '')
    name = models.CharField(max_length=200)
    store = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default = 1)
    brand = models.CharField(max_length=200)
    category =models.CharField(max_length=25,choices = category_choice, default = 'fruits')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(blank = True, null = True)
    # rating = models.DecimalField(default = 0,max_digits=2, decimal_places=1, blank = True, null = True)
    # numReviews = models.IntegerField(default = 0, blank = True, null = True)
    weight = models.CharField(max_length =20,blank = True,  null = True)
    volume = models.CharField(max_length =20,blank = True,  null = True)
    size = models.CharField(max_length =20, blank = True, null = True)
    color = models.CharField(max_length =20, blank = True, null = True)
    description = models.TextField(max_length =2000, blank = True, null = True)
    valtype = models.CharField(max_length =200, blank = True, null = True)

#remove category part

    def __str__(self):
        return self.name + ' by ' + str(self.store)


class SellerProductModel(models.Model):
    category_choice = (('electronics', 'electronics'),    ('vegetable', 'vegetable'),        ('cloth', 'cloth'),  ('fruits', 'fruits'),('furniture', 'Female'),  ('book', 'book'),        ('others', 'others'))
    img1 = models.ImageField(null=True, blank=True, upload_to = '')
    img2 = models.ImageField(null=True, blank=True, upload_to = '')
    img3 = models.ImageField(null=True, blank=True, upload_to = '')
    name = models.CharField(max_length=200)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default = 1)
    brand = models.CharField(max_length=200)
    category =models.CharField(max_length=25,choices = category_choice, default = 'fruits')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(blank = True, null = True)
    rating = models.DecimalField(default = 0,max_digits=2, decimal_places=1, blank = True, null = True)
    numReviews = models.IntegerField(default = 0, blank = True, null = True)
    weight = models.CharField(max_length =20,blank = True,  null = True)
    volume = models.CharField(max_length =20,blank = True,  null = True)
    size = models.CharField(max_length =20, blank = True, null = True)
    color = models.CharField(max_length =20, blank = True, null = True)
    valtype = models.CharField(max_length =200, blank = True, null = True)
    description = models.TextField(max_length =2000, blank = True, null = True)


    def __str__(self):
        return self.name + ' by ' + str(self.seller)


# class temp_model(models.Model):
#     name = models.CharField(max_length=25)
#     list = JSONField()


# # temp_model.objects.create(name='Rufus', data={
# #      'breed': 'labrador',
# #      'owner': {
# #          'name': 'Bob',
# #          'other_pets': [{
# #              'name': 'Fishy',
# #          }],
# #      },
# #  })