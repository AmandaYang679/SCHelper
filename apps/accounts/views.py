import requests, uuid
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config as config_env

from .models import EXBOUser
from .serializers import EXBOUserCreationSerializer


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
        "refresh_access_token": "refresh_access_token",
        "user_info": "user_info",
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
        elif uri == self.ROUTS["authorize"]:
            return "/oauth/authorize"
        elif uri == self.ROUTS["get_token"]:
            return "/oauth/token"
        elif uri == self.ROUTS["user_info"]:
            return "/oauth/user"
    
    
    def exbo_user_authorization(self):
        params = {
            "client_id": self.CLIENT_ID,
            "redirect_uri": self.REDIRECTED_URI,
            "scope": "",
            "response_type": "code",
            "state": uuid.uuid4()
        }
        return requests.get(reverse(self.BASE_URL + self._get_url_param(self.ROUTS["authorize"]), query=params))
    
    
    def get_token_from_code(self, code):
        params = {
        "client_id": self.CLIENT_ID,
        "client_secret": self.CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": self.REDIRECTED_URI
        }
        return requests.get(reverse(self._get_url(self._get_url_param(self.ROUTS["get_token"]), True), query=params))
    
    
    def refreshing_user_access_token(self, user_refresh_token):
        params = {
        "client_id": self.CLIENT_ID,
        "client_secret": self.CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": user_refresh_token,
        "scope": ""
        }
        return requests.post(reverse(self._get_url(self._get_url_param(self.ROUTS["get_token"]), True), query=params))

    
    def requesting_user_info(self, user_access_token):
        headers = {"Authorization": f"Bearer {user_access_token}"}
        return requests.get(reverse(self._get_url(self._get_url_param(self.ROUTS["user_info"]), True), headers=headers))
    
    
    def get_characters(self): # demo api
        headers = {"Authorization": f"Bearer {self.DEMO_USER_TOKEN}"}
        response = requests.get(self._get_url(self._get_url_param(self.ROUTS["characters"]), False), headers=headers)
        return response
    
    


class ExboAuthView(APIView):
    api = StalcraftAPI()
    def get(self, request):
        serializer = EXBOUserCreationSerializer()
        serializer.is_valid()
        
        response = self.api.exbo_user_authorization()
        code = response["code"]
        token_response = self.api.get_token_from_code(code)
        
        access_token = token_response["access_token"]
        refresh_token = token_response["refresh_token"]
        expires_in = token_response["expires_in"]
        
        user_info_response = self.api.requesting_user_info(access_token)
        
        user_id = user_info_response["id"]
        
        serializer.create(user_id, access_token, refresh_token, expires_in)
        
        return Response({"message": "user has been created successfully"})