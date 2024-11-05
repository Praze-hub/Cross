from customuser.enums import CustomEnum

class TruckStatus(CustomEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"

class IdOptions(CustomEnum):
    PASSPORT = "PASSPORT"
    LICENSE = "LICENSE"
    VOTERS_CARD = "VOTERS_CARD"
    NATIONAL_ID = "NATIONAL_ID"
    
class VerificatonStatus(CustomEnum):
    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"
    PROCESSING = "PROCESSING"
    
    

