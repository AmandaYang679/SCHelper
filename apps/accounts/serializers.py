from rest_framework import serializers

from .models import EXBOUser


class EXBOUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EXBOUser
        fields = ("user_id", "access_token", "refresh_token", "token_expires_in")

    def create(self, validated_data):
        user = EXBOUser.objects.create(**validated_data)
        return user
