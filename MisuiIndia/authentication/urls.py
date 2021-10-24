from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, RegisterView,  storeRegister,home,storeRegisterform, storelogin, storelogout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/obtain/', ObtainTokenPair.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # path('login/', loginView.as_view(), name='login'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', home, name = 'home'),
    path('storeRegister/', storeRegister.as_view(), name='storeRegister'),
    path('storeRegisterform/', storeRegisterform, name='storeRegisterform'),
    path('storelogin/', storelogin.as_view(), name='storelogin'),
    path('storelogout/', storelogout, name = 'storelogout'),
    path('order/',include('orders.urls')),
    path('product/',include('products_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)