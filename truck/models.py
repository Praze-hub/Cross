from django.db import models
from truck.enums import TruckStatus, IdOptions, VerificatonStatus
from customuser.models import User


class Driver(models.Model):
        user = models.OneToOneField(
            User,
            on_delete= models.CASCADE,   
            related_name= 'driver',
        )
        id_number = models.CharField(max_length=20, null=True, blank=True)
        id_type = models.CharField(max_length=100, choices=IdOptions.choices(), default=IdOptions.PASSPORT.value)
        vehicle_reg_no = models.CharField(max_length=20, null=True, blank=True)
        bank_name = models.CharField(max_length=200, null=True, blank=True)
        bank_code = models.CharField(max_length=10, null=True, blank=True)
        bank_account_number = models.CharField(max_length=100, null=True, blank=True)
        bank_account_name = models.CharField(max_length=100, null=True, blank=True)
        verificaton_status = models.CharField(max_length=100, choices=VerificatonStatus.choices(), default=VerificatonStatus.PROCESSING.value)
        
        def __str__(self):
            return f"{self.user.firstname} {self.user.lastname}"
        
        def verify(self):
            self.status = VerificatonStatus.VERIFIED.value
            self.save()
        
        def unverify(self):
            self.status = VerificatonStatus.UNVERIFIED.value
            self.save()
        
        def process(self):
            self.status =  VerificatonStatus.PROCESSING.value
            self.save() 
        

        
class Truck(models.Model):
    truck_name = models.CharField(max_length=255, unique=True)
    license_plate = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=40, choices=TruckStatus.choices(), default=TruckStatus.ACTIVE.value)
    model = models.CharField(max_length = 255)
    year_of_onboarding = models.DateField(auto_now_add=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="drivers", null=True)
    
    def  __str__(self):
        return self.truck_name
    
    def is_active(self):
        return self.status == TruckStatus.ACTIVE.value
    
    def activate(self):
        self.status = TruckStatus.ACTIVE.value
        self.save()
        
    def deactivate(self):
        self.status = TruckStatus.INACTIVE.value
        self.save()
        
    def set_maintenance(self):
        self.status = TruckStatus.MAINTENANCE.value
        self.save() 
        

