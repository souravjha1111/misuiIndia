from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from products_api.models import ProductModel,SellerProductModel
from authentication.models import CustomUser
from django.contrib.postgres.fields import ArrayField

class OrderModel(models.Model):
    OrderItems = models.CharField(max_length = 5000, null = True, blank = True)
    userid = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  blank = False)
    status = models.CharField(max_length = 200, blank = True, null = True)
    totalprice = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length =1000, blank = True)
    usern = models.CharField(max_length =100, blank = True)
    
    def __str__(self):
        return str(self.usern) + 'with user id '+ str(self.userid) + ' ordered  ' + str(self.OrderItems)


# {   
#     OrderItems:[

#        {id:"12346790",name:"tshirt",qty:"3",price:20,type:'L',color:'red'},
#        {id:"12346790",name:"maggie",qty:"2",price:30,type:'200g'},
#   
#   ],//array of objects
#     status:"delivered", //char
#     address:"M S R Nagar, MSRIT price, College Walkway Bengaluru, Karnataka 560054",//char
#     userid:"123467", //integer
#     usern: "sourav", //char
#     totalprice:12000 //integer
# }