import requests, uuid
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config as config_env

from .models import User
from .serializers import UserRegistrationSerializer


class StalcraftAPI(APIView):
    BASE_URL = config_env('BASE_URL')
    DEMO_BASE_URL = config_env('DEMO_BASE_URL')
    DEMO_APP_TOKEN = config_env('DEMO_APP_TOKEN')
    DEMO_USER_TOKEN = config_env('DEMO_USER_TOKEN')
    CLIENT_ID = config_env('CLIENT_ID')
    REDIRECTED_URI = config_env('REDIRECTED_URI')
    
    ROUTS = {
        "characters": "characters",
        "auth": "auth",
        "authorize": "authorize",
        "get_token": "get_token",
    }
    
    
    def _get_url(self, param, flag=False):
        if flag == True:
            url = self.BASE_URL + param
        else:
            url = self.DEMO_BASE_URL + param
        return url
    
    
    def _get_url_param(self, uri):
        if uri == self.ROUTS["characters"]:
            return "/RU/characters"
        if uri == self.ROUTS["authorize"]:
            return "/oauth/authorize"
        if uri == self.ROUTS["get_token"]:
            return "/oauth/token"
    
    
    def generate_redirect_url(self):
        params = {
            "client_id": self.CLIENT_ID,
            "redirect_uri": self.REDIRECTED_URI,
            "scope": "",
            "response_type": "code",
            "state": uuid.uuid4()
        }
        url = reverse(self.BASE_URL + self._get_url_param(self.ROUTS["authorize"]), query=params)
        print(url)
        return url
    
    
    def get_auth(self):
        # headers = {"Authorization": f"Bearer {self.DEMO_USER_TOKEN}"}
        return requests.get(self._get_url(self._get_url_param(self.ROUTS["auth"]), False))
    
    
    def get_characters(self):
        headers = {"Authorization": f"Bearer {self.DEMO_USER_TOKEN}"}
        response = requests.get(self._get_url(self._get_url_param(self.ROUTS["characters"]), False), headers=headers)
        return response
    
    


class ExboAuthView(APIView):
    def get(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # code = serializer.validated_data.get("code")
        # use_demo = serializer.validated_data.get("use_demo")

        api = StalcraftAPI()
        
        response = api.get_characters()
        profile = response.json()
        user_id = profile[0]["information"]["id"]
        user_nickname = profile[0]["information"]["nickname"]
        
        serializer.create('test', 'dfalaksdj123jl1k2kj1lk1klj', user_id, user_nickname, '12kjk2jk', '232dcj3', 36000, False, True, False, False)
        
        
        return Response({"message": "user has been created", "response": profile})