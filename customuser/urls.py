from django.urls import path, include
# from .views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import CustomTokenObtainPairView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/auth', include('django.contrib.auth.urls')), 
]