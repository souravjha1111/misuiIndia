from django import forms
from .models import ProductModel
class productregistrationform(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"



