from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['productName', 'seller', 'image','brand','category','price','countInStock','rating','numReviews']