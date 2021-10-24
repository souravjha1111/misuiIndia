from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import ProductModel, SellerProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['productName', 'store', 'image','brand','category','price','countInStock','rating','numReviews','weight','size','color', 'description']


class SellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProductModel
        fields = "__all__"
