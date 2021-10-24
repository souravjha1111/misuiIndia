from rest_framework import permissions
from .serializers import  ProductSerializer, SellerProductSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import QueryDict
from .models import ProductModel
from rest_framework.response import Response
from rest_framework import viewsets
from .forms import productregistrationform
import time
import jwt
from  authentication.models import CustomUser
class addnewproductdetails(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        print("#######################################################################################################")
        if not request.POST._mutable:
            request.POST._mutable = True
        data = request.data
        print("#######################################################################################################")       
        product_data = SellerProductSerializer(data=data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return render(request, 'products_api/home.html')
    
    def get(self, request):
        return render(request, 'products_api/addnewproductdetails.html')
       

class allproducts(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        Products = ProductModel.objects.all()
        serializer = ProductSerializer(Products,many = True)
        return Response(serializer.data)



class detailofproduct(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk):
        product = ProductModel.objects.get(pk = pk)
        serializer = SellerProductSerializer(product)
        return Response(serializer.data)



class getstoreproducts(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk):
        product = ProductModel.objects.all()
        product = product.filter(store = pk)
        serializer = SellerProductSerializer(product, many =True)

        return Response(serializer.data)



def home(request):
    return render(request, 'products_api/home.html')


def registerstoreproductsform(request):
    if request.method == 'POST':
        response = redirect('storelogin')
        print("#########################################################################")
        cookies = request.COOKIES
        decoded = []
        if 'refresh' in cookies:
            decoded = jwt.decode(cookies['refresh'], options={"verify_signature": False}) 
            if int(decoded['exp'] ) <int(time.time()):
                print("true")
                return response
        if 'refresh' not in cookies:
            return response
        response = redirect('storelogin')
        form = productregistrationform(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.store = CustomUser.objects.get(id = decoded["user_id"])
            form.save()
            return render(request, 'products_api/home.html')
    else:
        form = productregistrationform()
    return render(request, 'products_api/productregisterform.html', {'form': form})






###############################################################################################################################################
# def addnewproductdetails(request):
#     if request.method == 'POST':
#         product_data = SellerProductSerializer(data =data)
#         if form.is_valid():
#             form.save()
#             return redirect("home")   
#     else:
#         form = SellerProductSerializer()
#     return render(request, 'products_api/addnewproductdetails.html', {'form': form})



# class ProductRegister(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request):
#         form = SellerProductSerializer(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Your Product is registered")  

#     def get(self, request):
#         form = SellerProductSerializer()
#         return render(request, 'products_api/registerproduct.html', {'form': form})        











# # Create your views here.
# def registerstoreproductsform(request):
# 	context = {}
# 	if request.method == "POST":
# 		form = productregistrationform(request.POST, request.FILES)
# 		if form.is_valid():
# 			image = form.cleaned_data.get("image")
# 			productName = form.cleaned_data.get("productName")
# 			store = form.cleaned_data.get("store")
# 			brand = form.cleaned_data.get("brand")
# 			category = form.cleaned_data.get("category")
# 			price = form.cleaned_data.get("price")
# 			countInStock = form.cleaned_data.get("countInStock")
# 			rating = form.cleaned_data.get("rating")
# 			numReviews = form.cleaned_data.get("numReviews")
# 			weight = form.cleaned_data.get("weight")
# 			volume = form.cleaned_data.get("volume")
# 			size = form.cleaned_data.get("size")
# 			color = form.cleaned_data.get("color")
# 			description = form.cleaned_data.get("description")
# 			obj = GeeksModel.objects.create(image = image,	productName = productName,store = store,brand = brand,category = category,price = price, rating = rating, countInStock = countInStock, numReviews = numReviews,
# 								weight = weight, volume = volume, size = size, color = color, description = description)
# 			obj.save()
            
# Create your views here.