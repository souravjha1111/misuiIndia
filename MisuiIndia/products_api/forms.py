from django import forms
from .models import ProductModel
class productregistrationform(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["productName","image","price","category","brand","countInStock","weight","volume","size","color","description"]



