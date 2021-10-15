from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact_number = models.IntegerField(null=True, blank = True) #Edit this null part
    isSeller = models.BooleanField(default = False )
    adharCardNumber = models.BigIntegerField(unique = True, null = True, blank = True)
    PanNumber = models.CharField(unique  = True,  null = True, blank = True, max_length = 10)
    REQUIRED_FIELDS = ['password','contact_number']
    
    def __str__(self):
        return str(self.username)