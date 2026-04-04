from rest_framework import serializers

from .models import EXBOUser


class EXBOUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EXBOUser
        fields = "__all__"

    def create(self, validated_data):
        user, _ = EXBOUser.objects.update_or_create(
            user_id=validated_data["user_id"],
            defaults=validated_data
        )
        return user
