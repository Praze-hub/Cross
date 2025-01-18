from customuser.enums import CustomEnum

class TaskStatus(CustomEnum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    
class TaskPriority(CustomEnum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    
class TaskType(CustomEnum):
    PICKUP = "PICKUP"
    DELIVERY = "DELIVERY"
    MAINTENANCE = "MAINTENANCE"
    OTHER = "OTHER"
    


    