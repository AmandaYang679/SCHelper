from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ItemsBuildSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateItemsBuild(APIView):
    def post(self, request):
        serializer = ItemsBuildSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    