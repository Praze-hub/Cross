from django.db import models
from .enums import TaskPriority, TaskStatus, TaskType
from truck.models import Truck


class Task(models.Model):
    task_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    task_type = models.CharField(
        max_length=20,
        choices=TaskType.choices(),
        default=TaskType.OTHER.value,
    )
    priority = models.CharField(
        max_length=20,
        choices=TaskPriority.choices(),
        default=TaskPriority.MEDIUM.value,
    )
    task_status = models.CharField(
        max_length=255,
        choices=TaskStatus.choices(),
        default=TaskStatus.PENDING.value,
        
    )
    location = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        Truck,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

    class Meta:
        ordering = ["-priority", "due_date"]
    
    #TASK STATUS    
    def mark_as_completed(self):
        """Mark the task as completed."""
        self.status = TaskStatus.COMPLETED
        self.save()

    def cancel(self):
        """Cancel the task."""
        self.status = TaskStatus.CANCELLED
        self.save()

    def start_progress(self):
        """Mark the task as in progress."""
        self.status = TaskStatus.IN_PROGRESS
        self.save()
        
    def pending(self):
        """Mark the task as pending."""
        self.status = TaskStatus.PENDING
        self.save()
        
    def failed(self):
        """Mark the task as failed."""
        self.status = TaskStatus.FAILED
        self.save()
        
    #TASK PRIORITY
    def high_priority(self):
        self.status = TaskPriority.HIGH
        self.save()
        
    def medium_priority(self):
        self.status = TaskPriority.MEDIUM
        self.save()
        
    def low_priority(self):
        self.status = TaskPriority.LOWOW
        self.save()
        
    #TASK TYPE
    def pickup(self):
        self.status = TaskType.PICKUP
        self.save()
        
    def maintenance(self):
        self.status = TaskType.MAINTENANCE
        self.save()
        
    def delivery(self):
        self.status = TaskType.DELIVERY
        self.save()
        
    def other(self):
        self.status = TaskType.OTHER
        self.save()