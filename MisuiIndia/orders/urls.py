from django.urls import path
from .views import  allOrders, orderResgister, allOrdersOfUser

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('orderresgister/', orderResgister.as_view(), name='orderresgister'),
    path('allOrders/', allOrders.as_view(), name='allOrders'),
    path('allOrdersOfUser/<str:pk>/', allOrdersOfUser.as_view(), name='allOrdersOfUser'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          