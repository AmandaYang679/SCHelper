from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import *


class ItemListView(APIView):
    serializers = {
        "weapon-assault-rifle": AssaultRifleWeaponItemSerializer,
        "weapon-device": DeviceWeaponItemSerializer,
        "medicine": MedicineItemSerializer,
    }

    def get_serializer_for_category(self, category):
        if not category:
            return BaseItemSerializer

        for key, serializer in self.serializers.items():
            if key in category.lower():
                return serializer

        return BaseItemSerializer

    def get(self, request):
        name = request.GET.get("name")
        category = request.GET.get("category")
        rank = request.GET.get("rank")

        filters = {}
        if category:
            filters["category"] = category
        if name:
            filters["name"] = name
        if rank:
            filters["rank"] = rank

        items = Item.objects.filter(**filters)
        # items = Item.objects.filter(category="medicine")
        response = []
        for item in items:
            serializer_class = self.get_serializer_for_category(item.category)
            serializer = serializer_class(item)
            response.append(serializer.data)
        return Response(response)
