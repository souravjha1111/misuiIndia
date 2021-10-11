from django import forms
from .models import ProductModel


class SellerRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['productName', 'seller', 'image','brand','category','price','countInStock','rating','numReviews']

#