from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import  addnewproductdetails, home, allproducts, detailofproduct

urlpatterns = [
    path('addnewproductdetails/', addnewproductdetails.as_view(), name='addnewproductdetails'),
    path('allproducts/', allproducts.as_view(), name='getallproducts'),
    path('detailofproduct/<str:pk>/', detailofproduct.as_view(), name='detailofproduct'),
    path('home/', home, name = 'home')
]