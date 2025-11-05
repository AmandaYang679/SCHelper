from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import *
import json
from .infoblocks.weapon_infoblock.assault_rifle import Assault_rifle
from .infoblocks.aggregate import Aggregate


class ItemListView(APIView):
    serializers = {
        "weapon/assault_rifle": AssaultRifleWeaponItemSerializer,
    }

    def get_serializer_for_category(self, category):
        if not category:
            return BaseItemSerializer

        for key, serializer in self.serializers.items():
            if key in category.lower():
                return serializer

        return BaseItemSerializer

    def get(self, request):
        en_name = request.GET.get("en_name")
        category = request.GET.get("category")
        en_rank = request.GET.get("en_rank")

        # filters = {}
        # if category:
        #     filters["category"] = category
        # if en_name:
        #     filters["en_name"] = en_name
        # if en_rank:
        #     filters["en_rank"] = en_rank

        # items = Item.objects.filter(**filters)
        items = Item.objects.filter(category="medicine")
        response = []
        for item in items:
        # serializer_class = self.get_serializer_for_category(category)
            serializer = MedicineItemSerializer(item)
            response.append(serializer.data)
        return Response(response)
