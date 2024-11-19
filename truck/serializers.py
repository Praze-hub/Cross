from rest_framework import serializers
from .models import Driver, VerificatonStatus
from truck.enums import IdOptions, VerificatonStatus

class DriverSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    id_type = serializers.ChoiceField(choices=IdOptions.choices())
    verification_status = serializers.ChoiceField(choices=VerificatonStatus.choices(), read_only=True)
    
    class Meta:
        model = Driver
        fields = [
            'id',
            'user_username',
            'user_email',
            'id_number',
            'id_type',
            'vehicle_reg_no', 
            'bank_name', 
            'bank_code', 
            'bank_account_number', 
            'bank_account_name', 
            'verification_status',
        ]