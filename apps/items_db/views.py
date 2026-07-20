from django.shortcuts import render
from rest_framework.views import APIView
from .models import Item


class GetItems(APIView):
    def get(self, request):
        items = Item.objects.all()
        return items
