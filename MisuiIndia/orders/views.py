from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import OrderSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.views import APIView
import jwt, datetime
from django.views import View
from .models import OrderModel, SellerProductModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.conf import settings



class orderResgister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class allOrders(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        Products = OrderModel.objects.all()
        serializer = OrderSerializer(Products,many = True)
        return Response(serializer.data)



class allOrdersOfUser(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk):
        product = OrderModel.objects.get(pk = pk)
        serializer = OrderSerializer(product)
        return Response(serializer.data)
