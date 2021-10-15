from rest_framework import permissions
from .serializers import  ProductSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import QueryDict
from .models import ProductModel
from rest_framework.response import Response
from rest_framework import viewsets
from .forms import productregistrationform


class addnewproductdetails(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        print("#######################################################################################################")
        if not request.POST._mutable:
            request.POST._mutable = True
        data = request.data
        # data['seller'] = request.user.id
        print(data['seller'])
        print("#######################################################################################################")       
        product_data = ProductSerializer(data=data)
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
        serializer = ProductSerializer(product)
        return Response(serializer.data)



class getsellerproducts(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk):
        product = ProductModel.objects.all()
        product = product.filter(seller = pk)
        serializer = ProductSerializer(product, many =True)

        return Response(serializer.data)



def home(request):
    return render(request, 'products_api/home.html')


def registersellerproductsform(request):
    if request.method == 'POST':
        form = productregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'products_api/home.html')

    else:
        form = productregistrationform()
    return render(request, 'products_api/productregisterform.html', {'form': form})




# # Create your views here.
# def registersellerproductsform(request):
# 	context = {}
# 	if request.method == "POST":
# 		form = productregistrationform(request.POST, request.FILES)
# 		if form.is_valid():
# 			image = form.cleaned_data.get("image")
# 			productName = form.cleaned_data.get("productName")
# 			seller = form.cleaned_data.get("seller")
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
# 			obj = GeeksModel.objects.create(image = image,	productName = productName,seller = seller,brand = brand,category = category,price = price, rating = rating, countInStock = countInStock, numReviews = numReviews,
# 								weight = weight, volume = volume, size = size, color = color, description = description)
# 			obj.save()
            
# Create your views here.
def registersellerproductsform(request):
    if request.method == "POST":
        form = productregistrationform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
    else:
        form = productregistrationform()
    return render(request, 'products_api/productregisterform.html', {'form': form})



            # image = form.cleaned_data.get("image")
            # productName = form.cleaned_data.get("productName")
			# seller = form.cleaned_data.get("seller")
            # brand = form.cleaned_data.get("brand")
			# category = form.cleaned_data.get("category")
			# price = form.cleaned_data.get("price")
			# countInStock = form.cleaned_data.get("countInStock")
			# rating = form.cleaned_data.get("rating")
			# numReviews = form.cleaned_data.get("numReviews")
			# weight = form.cleaned_data.get("weight")
			# volume = form.cleaned_data.get("volume")
			# size = form.cleaned_data.get("size")
			# color = form.cleaned_data.get("color")
			# description = form.cleaned_data.get("description")
            # obj = GeeksModel.objects.create(image = image,	productName = productName,seller = seller,brand = brand,category = category,price = price, rating = rating, countInStock = countInStock, numReviews = numReviews,
			# 					weight = weight, volume = volume, size = size, color = color, description = description)

###############################################################################################################################################
# def addnewproductdetails(request):
#     if request.method == 'POST':
#         product_data = ProductSerializer(data =data)
#         if form.is_valid():
#             form.save()
#             return redirect("home")   
#     else:
#         form = ProductSerializer()
#     return render(request, 'products_api/addnewproductdetails.html', {'form': form})



# class ProductRegister(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def post(self, request):
#         form = ProductSerializer(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Your Product is registered")  

#     def get(self, request):
#         form = ProductSerializer()
#         return render(request, 'products_api/registerproduct.html', {'form': form})        