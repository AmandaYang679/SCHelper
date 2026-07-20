from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config as config_env
from .services.exbo_client import ExboClientAPI
from .models import EXBOUser
from .serializers import EXBOUserSerializer


REGIONS = ["ru", "eu", "sea", "nea"]
client = ExboClientAPI()


class ExboAuthView(APIView):
    def get(self, request):
        return client.authorize(request)
    

class ExboCallbackView(APIView):
    def get(self, request):
        code = request.GET.get("code")
        return client.call_back(request, code)
    

class ExboRefreshAccessToken(APIView):
    def get(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("exbo_auth")
        user = EXBOUser.objects.get(user_id = request.session.get("user_id"))
        response = client.refresh_access_token(request, user)
        return Response(response)

        
class CharacterProfile(APIView):
    def get(self, request):
        for region in REGIONS:
            response = client.get_characters_by_region(request, region)
            if isinstance(response, list):
                if len(response) == 0:
                    continue
                if len(response) > 1:
                    profile = []
                    for index_character in range(len(response)):
                        profile.append(
                            client.get_character_profile(request, region, response[index_character]["information"]["name"])
                        )
                    return Response(profile)
                else:
                    profile = client.get_character_profile(request, region, response[0]["information"]["name"])
                    return Response(profile)
            elif isinstance(response, dict):
                continue
        return Response({"error": "character not found"})
        
    
class GetPlayerCharacters(APIView):
    def get(self, request):  
        for region in REGIONS:
            response = client.get_characters_by_region(request, region)
            if type(response) == list:
                return Response(response)
            elif type(response) == dict:
                return Response((response["title"], response["status"]))
        return Response({"error": "user not found"})
    
    
class GetPlayerEmissionStatus(APIView):
    def get(self, request):
        for region in REGIONS:
            response = client.get_character_emission(request, region)
            if response:
                return Response(response)
            
            
class GetFriendList(APIView):
    def get(self, request):
        friends = []
        for region in REGIONS:
            name = client.get_character_name(request, region)
            if not name:
                continue
            response = client.get_friend_list(request, region, name)
            friends.append(response)
        return Response(friends)
