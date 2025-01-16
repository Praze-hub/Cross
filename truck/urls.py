from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, TruckViewSet

router=DefaultRouter()
router.register('drivers', DriverViewSet, basename='driver')
router.register('truck', TruckViewSet, basename='truck')

urlpatterns = [
    path('', include(router.urls)),
]