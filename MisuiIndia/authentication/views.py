from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer, UserSerializer, SellerSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SellerRegisterForm
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView


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
       
def home(request):
    return render(request, 'products_api/home.html')


#################################################################################################################################################

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





# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username = username, password = password)      

#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponseRedirect('/accounts/invalid')