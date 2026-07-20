import uuid, requests
from urllib.parse import urlencode
from decouple import config as config_env
from django.shortcuts import redirect
from apps.accounts.models import EXBOUser
from apps.accounts.serializers import EXBOUserSerializer
from rest_framework.response import Response
from rest_framework import status



BASE_URL = config_env('BASE_URL')
EAPI = config_env('EAPI')
CLIENT_ID = config_env('CLIENT_ID')
REDIRECTED_URI = config_env('REDIRECTED_URI')
CLIENT_SECRET = config_env('CLIENT_SECRET')
REGIONS = ["eu", "ru", "sea", "nea"]


class ExboClientAPI():
    def authorize(self, request):
        state = str(uuid.uuid4())
        request.session["state"] = state

        params = {
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECTED_URI,
            "response_type": "code",
            "scope": "",
            "state": state
        }

        url = BASE_URL + "oauth/authorize"
        return redirect(f"{url}?{urlencode(params)}")
    

    def call_back(self, request, code):
        state = request.GET.get("state")
        session_state = request.session.get("state")
        
        if session_state != state:
            return Response(
                {"error": "Invalid OAuth state"},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.session.pop("oauth_state", None)
        
        params={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECTED_URI
            }
        
        token_response = requests.post(BASE_URL + "oauth/token", data=params)
        token_data = token_response.json()
        
        access_token = token_data["access_token"]
        refresh_token = token_data["refresh_token"]
        expires_in = token_data["expires_in"]
        
        user_data = self._api_client_exbo(request, access_token, "oauth/user")
        
        # session
        request.session["user_id"] = user_data["id"]
        request.session["access_token"] = access_token
        serializer = EXBOUserSerializer(
            data={
                "user_id": user_data["id"],
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_expires_in": expires_in,
            }
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def refresh_access_token(self, request, user: EXBOUser):
        params={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "grant_type": "refresh_token",
                "refresh_token": user.refresh_token,
                "scope": ""
            }
        response = requests.post(BASE_URL + "oauth/token", data=params).json()
        
        user.access_token = response["access_token"]
        user.refresh_token = response["refresh_token"]
        user.save()
        request.session["access_token"] = response["access_token"]
        
        return {"response": "token was successfully updated"}
            
        
    def get_characters_by_region(self, request, region):
        access_token = self._get_access_token(request)
        response = self._api_client_eapi(request, access_token, f"{region}/characters")
        # test error answer
        # response = requests.get(EAPI + f"{region}/characters")
        return response
    
    
    def get_character_profile(self, request, region, character):
        access_token = self._get_access_token(request)
        response = self._api_client_eapi(request, access_token, f"{region}/character/by-name/{character}/profile")
        return response
    
    
    def get_character_emission(self, request, region):
        access_token = self._get_access_token(request)
        response = self._api_client_eapi(request, access_token, f"{region}/emission")
        return response
    
    
    def get_friend_list(self, request, region, character):
        access_token = self._get_access_token(request)
        response = self._api_client_eapi(request, access_token, f"{region}/friends/{character}")
        return response
    
    
    def get_character_name(self, request, region):
        response = self.get_characters_by_region(request, region)
        if response:
            name = response[0]["information"]["name"]
            return name
            
    
    def _get_access_token(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("exbo_auth")
        user = EXBOUser.objects.get(user_id=user_id)
        return user.access_token
    
    
    def _get_regions(self):
        response = requests.get(EAPI + "regions")
        return Response(response)
    
    
    def _api_client_exbo(self, request, access_token, url):
        response = requests.get(
            BASE_URL + url,
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return response.json()
    
    
    def _api_client_eapi(self, request, access_token, url):
        response = requests.get(
            EAPI + url,
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return response.json()