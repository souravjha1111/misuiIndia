from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, RegisterView,  SellerRegister,home

urlpatterns = [
    path('token/obtain/', ObtainTokenPair.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # path('login/', loginView.as_view(), name='login'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', home, name = 'home'),
    path('SellerRegister/', SellerRegister.as_view(), name='SellerRegister'),
    path('product/',include('products_api.urls'))
]