from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "ru_name", "en_name", "icon", "category", "color", "status", "status", "infoblocks")
        read_only_fields = ("id", "ru_name", "en_name", "icon", "category", "color", "status", "status", "infoblocks")
