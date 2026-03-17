import uuid, requests
from urllib.parse import urlencode
from decouple import config as config_env
from django.shortcuts import redirect
from apps.accounts.serializers import EXBOUserCreationSerializer
from rest_framework.response import Response
from rest_framework import status


BASE_URL = config_env('BASE_URL')
CLIENT_ID = config_env('CLIENT_ID')
REDIRECTED_URI = config_env('REDIRECTED_URI')
CLIENT_SECRET = config_env('CLIENT_SECRET')


class ExboClientAPI():
    def authorize(self):
        state = str(uuid.uuid4())

        params = {
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECTED_URI,
            "response_type": "code",
            "scope": "",
            "state": state
        }

        url = BASE_URL + "authorize"
        return redirect(f"{url}?{urlencode(params)}")


    def call_back(self, code):
        params={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECTED_URI
            }
        
        token_response = requests.post(BASE_URL + "token", data=params)
        token_data = token_response.json()
        
        access_token = token_data["access_token"]
        refresh_token = token_data["refresh_token"]
        expires_in = token_data["expires_in"]
        
        user_response = requests.get(
            BASE_URL + "user",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        
        user_data = user_response.json()
        serializer = EXBOUserCreationSerializer(
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