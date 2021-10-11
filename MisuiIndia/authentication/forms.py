from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SellerRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','contact_number','email','isSeller','PanNumber','adharCardNumber']



# class LoginForm(forms.Form):
#     username = forms.CharField(label='username', max_length=100)
#     password = forms.CharField(widget = forms.PasswordInput())
