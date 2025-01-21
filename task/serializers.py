from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task_id',
            'title',
            'description',
            'task_status',
            'priority',
            'location',
            'task_type',
            'due_date',
            'assigned_to',
            'created_at',
            'updated_at',
        ]
        
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        def validate_status(self, value):
            valid_statuses = ['pending', 'in_progress', 'completed', 'canceled', 'failed']
            if value not in valid_statuses:
                raise serializers.ValidationError(f"invalid status '{value}'. Valid options are {valid_statuses}.")
            return value
        
        def validate_priority(self, value):
            valid_priorities = ['low', 'medium', 'high']
            if value not in valid_priorities:
                raise serializers.ValidationError(f"invalid status '{value}'. Valid options are {valid_priorities}.")
            return value
        
        def validation_type(self, value):
            valid_types = ['pickup', 'delivery', 'maintenance']
            if value not in valid_types:
                raise serializers.ValidationError(f"invalid status '{value}'. Valid options are {valid_types}.")
            return value
        
        def validate(self, data):
            if data.get('status') == 'completed' and data.get('priority') == 'low':
                raise serializers.ValidatiionError("Completed tasks cannot have a low priority")
            return data

                
            