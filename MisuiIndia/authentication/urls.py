from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, RegisterView,  SellerRegister,home,SellerRegisterform, Sellerlogin, sellerlogout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/obtain/', ObtainTokenPair.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # path('login/', loginView.as_view(), name='login'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', home, name = 'home'),
    path('SellerRegister/', SellerRegister.as_view(), name='SellerRegister'),
    path('SellerRegisterform/', SellerRegisterform, name='SellerRegisterform'),
    path('Sellerlogin/', Sellerlogin.as_view(), name='Sellerlogin'),
    path('sellerlogout/', sellerlogout, name = 'sellerlogout'),
    path('order/',include('orders.urls')),
    path('product/',include('products_api.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
