from rest_framework import serializers
from .models import Maintenance
from .enums import MaintenanceStatus, MaintenanceType
from datetime import date

class MaintenanceSerializer(serializers.ModelSerializer):
    maintenance_status = serializers.ChoiceField(choices=MaintenanceStatus.choices(), default=MaintenanceStatus.OTHER.value)
    maintenance_type = serializers.ChoiceField(choices=MaintenanceType.choices(), default=MaintenanceType.OTHER.value)
    
    class Meta:
        model = Maintenance
        fields = '__all__'
        
    def validate_scheduled_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Scheduled date cannot be in the past")
        return value
    
    def validate_maintenance_value(self, value):
        if not value.strip():
            raise serializers.ValidationError("Maintenance venue cannot be empty")
        return value
             
    