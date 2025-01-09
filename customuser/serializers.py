from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
 