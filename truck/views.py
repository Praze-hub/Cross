# views.py
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer
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