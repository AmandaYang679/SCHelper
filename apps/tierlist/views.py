from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


class ItemListView(APIView):
    def get(self, request):
        category = request.GET.get("category")
        subcategory = request.GET.get("subcategory")

        items = Item.objects.all()
        if category:
            items = items.filter(category=category)
        if subcategory:
            items = items.filter(subcategory=subcategory)

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
