from rest_framework import serializers
from .models import Driver, Truck
from truck.enums import IdOptions, VerificatonStatus, TruckStatus

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
            'user',
        ]
        
        read_only_fields = ['user']  # Prevent the user field from being manually set

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user  # Assign the currently authenticated user
        return super().create(validated_data)
    
    
class TruckSerializer(serializers.ModelSerializer):
        status = serializers.ChoiceField(choices=TruckStatus.choices(), read_only=True)
        
        class Meta:
            model = Truck
            fields = [
                'truck_name',
                'license_plate',
                'model',
                'status',
                'year_of_onboarding',
                'driver'
            ]
            
    