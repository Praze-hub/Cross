from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Truck


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @csrf_exempt
    @action(
        detail=False, 
        methods=['get'], 
        serializer_class=TaskSerializer, 
        url_path="filter"
        )
    
    def filter(self, request):
        status_param = request.query_params.get('status')
        priority_param = request.query_params.get('priority')
        type_param = request.query_params.get('type')
        
        tasks = self.queryset
        
        if status_param:
            tasks = tasks.filter(status=status_param)
            
        if priority_param:
            tasks = tasks.filter(priority=priority_param)
            
        if type_param:
            tasks  = tasks.filter(type=type_param)
            
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    @action(
        detail=True, 
        methods=['post'], 
        serializer_class=TaskSerializer, 
        url_path="assign"
        )
    def assign(self, request, pk=None):
        task = self.get_object()
        truck_id = request.data.get('assigned_to')

        
        if not truck_id:
            return Response(
                {"error": "You must provide 'assigned_to' field."},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        truck = get_object_or_404(Truck, pk=truck_id)  # Fetch the Truck instance

        task.assigned_to = truck
        task.save()
        return Response(
            {'detail': 'Task assigned successfully'},
            status=status.HTTP_200_OK,
        )
        
    @csrf_exempt
    @action(
        detail=True, 
        methods=['post'], 
        serializer_class=TaskSerializer, 
        url_path="complete"
        )
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == 'completed':
            return Response(
                {'message': 'Task is already completed'},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        task.status = 'completed'
        task.save()
        return Response(
            {'message': 'Task marked as completed'},
            status=status.HTTP_200_OK,
        )
    
    
            
    
    

