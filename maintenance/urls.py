from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MaintenanceViewSet

router = DefaultRouter()
router.register('maintenance', MaintenanceViewSet, basename='maintenance')

urlpatterns = [
    path('', include(router.urls)),
]