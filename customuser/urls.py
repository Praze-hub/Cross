from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),    # Verify Token
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/auth', include('django.contrib.auth.urls')), 
]