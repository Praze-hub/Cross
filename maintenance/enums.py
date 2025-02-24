from customuser.enums import CustomEnum

class MaintenanceStatus(CustomEnum):
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    OTHER = "OTHER"
    
class MaintenanceType(CustomEnum):
    FULL_MAINTENANCE = "FULL_MAINTENANCE"
    PART_MAINTENANCE = "PART_MAINTENANCE"
    OTHER = "OTHER"
