from django.db import models
from .enums import MaintenanceStatus, MaintenanceType
from truck.models import Truck

class Maintenance(models.Model):
    maintenance_id = models.CharField(max_length=20, unique=True)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True)
    maintenance_type = models.CharField(max_length=40, choices=MaintenanceType.choices(), default=MaintenanceType.OTHER.value)
    maintenance_status = models.CharField(max_length=40, choices=MaintenanceStatus.choices(), default=MaintenanceStatus.OTHER.value)
    scheduled_date = models.DateField()
    maintenance_venue = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Maintenance {self.maintenance_id} - {self.maintenance_status}"
    
    def update_status(self, new_status):
        if new_status in MaintenanceStatus.values:
            self.maintenance_status = new_status
            self.save()
        else:
            raise ValueError(f"Invalid status '{new_status}'. Valid options: {MaintenanceStatus.values}")
        
        
    def update_type(self, new_type):
        """Update the maintenance type."""
        if new_type in MaintenanceType.values:
            self.maintenance_type = new_type
            self.save()
        else:
            raise ValueError(f"Invalid type '{new_type}'. Valid options: {MaintenanceType.values}")

    
    