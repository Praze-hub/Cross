from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Maintenance
from .serializers import MaintenanceSerializer
from .enums import MaintenanceStatus, MaintenanceType


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    
    @action(
        detail=True,
        methods=['post'],
        serializer_class=MaintenanceSerializer,
        url_path='update-status'
        )
    def update_status(self, request, pk=None):
        maintenance = self.get_object()
        new_status = request.data.get('maintenance_status')
        
        if new_status not in MaintenanceStatus.values():
            return Response({'error': "Invalid status provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        maintenance.maintenance_status = new_status
        maintenance.save()
        return Response({"message": "Maintenance status updated successfully"}, status=status.HTTP_200_OK)
    
    
    @action(
        detail=True,
        methods=['post'],
        serializer_class=MaintenanceSerializer,
        url_path='update-type'
        )
    def update_type(self, request, pk=None):
        maintenance = self.get_object()
        new_type = request.data.get('maintenance_type')
        
        if new_type not in MaintenanceType.values():
            return Response({'error': 'Invalid type provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        maintenance.maintenance_type = new_type
        maintenance.save()
        return Response({'message': 'Maintenance type updated succesfully'}, status=status.HTTP_200_OK)
    