from rest_framework import serializers
from .models import Build


class ItemsBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = "__all__"
    
    def create(self, validated_data):
        items = validated_data.pop("items_id")
        build = Build.objects.create(**validated_data)
        build.items_id.set(items)
        return build