from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import  addnewproductdetails, home, allproducts, detailofproduct, getstoreproducts, registerstoreproductsform

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('addnewproductdetails/', addnewproductdetails.as_view(), name='addnewproductdetails'),
    path('allproducts/', allproducts.as_view(), name='getallproducts'),
    path('detailofproduct/<str:pk>/', detailofproduct.as_view(), name='detailofproduct'),
    path('getstoreproducts/<str:pk>/', getstoreproducts.as_view(), name='getstoreproducts'),
    path('registerstoreproductsform/', registerstoreproductsform, name='registerstoreproductsform'),
    path('home/', home, name = 'home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            