# views.py
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Driver, Truck
from .serializers import DriverSerializer, TruckSerializer
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
    @csrf_exempt
    @action(
        detail=True, 
        methods=['post'], 
        serializer_class=DriverSerializer, 
        url_path="verify"
        )
    def verify(self, request, pk=None):
        driver = self.get_object()
        driver.verify()
        return Response({'status': 'Driver verified'}, status=status.HTTP_200_OK)
    
    @csrf_exempt
    @action(
        detail=True,
        methods=['post'], 
        serializer_class=DriverSerializer, 
        url_path="unverify"
        )
    def unverify(self, request, pk=None):
        driver = self.get_object()
        driver.unverify()
        return Response({'status': 'Driver unverified'}, status=status.HTTP_200_OK)
    
    @csrf_exempt
    @action(detail=True,
            methods=['post'], 
            serializer_class=DriverSerializer,
            url_path='process'
            )
    def process(self, request, pk=None):
        driver = self.get_object()
        driver.process()
        return Response({'status': 'Driver processing started'}, status=status.HTTP_200_OK)
    
    
class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    
    @csrf_exempt
    @action(
        detail = True,
        methods = ['post'],
        serializer_class = TruckSerializer,
        url_path = "activate"
    )
    def activate(self, request, pk=None):
        truck = self.get_object()
        truck.activate()
        return Response({'status': 'Truck activated'}, status=status.HTTP_200_OK)
    
    
    @csrf_exempt
    @action(
        detail = True,
        methods = ['post'],
        serializer_class = TruckSerializer,
        url_path = "deactivate"
    )
    def deactivate(self, request, pk=None):
        truck = self.get_object()
        truck.deactivate()
        return Response({'status': 'Truck deactivated'}, status=status.HTTP_200_OK)
    
    
    @csrf_exempt
    @action(
        detail = True,
        methods = ['post'],
        serializer_class = TruckSerializer,
        url_path = "maintenance"
    )
    def maintenance(self, request, pk=None):
        truck = self.get_object()
        truck.set_maintenance()
        return Response({'status': 'Truck set to maintenance'}, status=status.HTTP_200_OK)