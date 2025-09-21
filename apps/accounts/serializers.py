from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'exbo_user_id', 'exbo_username', 'exbo_access_token', 'exbo_refresh_token', 'exbo_token_expires_at', 'is_admin', 'is_admin', 'is_staff', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
    
    