from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer, UserSerializer, SellerSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SellerRegisterForm, sellerloginform
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import jwt, datetime
from django.views import View
from .models import CustomUser
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response



class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class SellerRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        seller = SellerSerializer(data=request.data)
        print(request.data.get('isSeller'))
        seller.is_valid(raise_exception=True)
        seller.save()
        return redirect(home) #redirect to login 
    
    def get(self, request):
        return render(request, 'authentication/sellerregister.html')



#HOME VIEW        
def home(request):
    return render(request, 'products_api/home.html')


def SellerRegisterform(request):
    if request.method == "POST":
        form = SellerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Sellerlogin')
    else:
        form = SellerRegisterForm()
    return render(request, 'authentication/sellerlogin.html', {'form': form})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class Sellerlogin(View):
    def post(self, request, format=None):
        form = sellerloginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                html = redirect('registersellerproductsform')
                data = get_tokens_for_user(user)
                html.set_cookie("access", data["access"])
                html.set_cookie( "refresh", data["refresh"])
                print(data)
                return html
            else:
                return HttpResponse("No active This account is not active!!")
        else:
            return HttpResponse("Incorrect creditentails")

    def get(self, request):
        form = sellerloginform()
        return render(request, 'authentication/sellerlogin.html', {'form': form})


########################################## SELLER LOGOUT BY DELETING COOKIES ######################
def sellerlogout(request):
    response = redirect('Sellerlogin')
    print("#########################################################################")
    response.delete_cookie('access')
    response.delete_cookie('refresh')
    return response
#################################################################################################################################################




# class loginView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request):
#         return redirect('token_create')



# def SellerRegister(request):
#     if request.method == 'POST':
#         form = SellerRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return HttpResponse("Your account has been created please login there")
#     else:
#         form = SellerRegisterForm()
#     return render(request, 'authentication/register.html', {'form': form})



# class loginView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request):
#         return redirect('token_create')




# def sellerlogin(request):
#     if request.method == "POST":
#         form = sellerloginform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             data = {
#                 username = ""
#             }
#             token = 

# class Sellerlogin(View):
#     def post(self, request):
#         form = sellerloginform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
 
#         user = CustomUser.objects.filter(username=username).first()

#         if user is None:
#             raise AuthenticationFailed('Enter correct email/username')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = None
#         token = jwt.encode(payload, 'secret', algorithm='HS256')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         if token ==None:
#             print("#########################  ##############") 
#         print("#######################################", "logged in", token)
#         print(response.data)
#         return JsonResponse(response.data)

#     def get(self, request):
#         form = sellerloginform()
#         return render(request, 'authentication/sellerlogin.html', {'form': form})


