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
        return redirect(home) 
    
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



def home(request):
    return render(request, 'products_api/home.html')


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