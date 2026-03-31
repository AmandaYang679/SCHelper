from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config as config_env
from .services.exbo_client import ExboClientAPI
from .models import EXBOUser
from .serializers import EXBOUserSerializer


class ExboAuthView(APIView):
    def get(self, request):
        client = ExboClientAPI()
        return client.authorize()
    

class ExboCallbackView(APIView):
    def get(self, request):
        code = request.GET.get("code")
        client = ExboClientAPI()
        return client.call_back(request, code)
        

class GetAllUsers(APIView):
    def get(self, request):
        users = EXBOUser.objects.all()
        serializer = EXBOUserSerializer(users, many=True)
        return Response({"users": serializer.data})
    

class UserProfile(APIView):
    def get(self, request):
        user_id = request.session.get("exbo_user_id")
        if user_id:
            user = EXBOUser.objects.get(user_id=user_id)
            serializer = EXBOUserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            return redirect("exbo-auth")
        
        
# class StalcraftAPI(APIView):
    
#     ROUTS = {
#         "characters": "characters",
#         "auth": "auth",
#         "authorize": "authorize",
#         "get_token": "get_token",
#         "refresh_access_token": "refresh_access_token",
#         "user_info": "user_info",
#     }
    
    
#     def _get_url(self, param, flag=True):
#         if flag == True:
#             url = self.BASE_URL + param
#         else:
#             url = self.DEMO_BASE_URL + param
#         return url
    
    
#     def _get_url_param(self, uri):
#         if uri == self.ROUTS["characters"]:
#             return "/RU/characters"
#         elif uri == self.ROUTS["authorize"]:
#             return "/oauth/authorize"
#         elif uri == self.ROUTS["get_token"]:
#             return "/oauth/token"
#         elif uri == self.ROUTS["user_info"]:
#             return "/oauth/user"
    
    
#     def exbo_user_authorization(self):
#         params = {
#             "client_id": self.CLIENT_ID,
#             "redirect_uri": self.REDIRECTED_URI,
#             "scope": "",
#             "response_type": "code",
#             "state": uuid.uuid4()
#         }
#         url = self.BASE_URL + self._get_url_param(self.ROUTS["authorize"])
#         return requests.get(url, params=params)
    
    
#     def get_token_from_code(self, code):
#         params = {
#         "client_id": self.CLIENT_ID,
#         "client_secret": self.CLIENT_SECRET,
#         "code": code,
#         "grant_type": "authorization_code",
#         "redirect_uri": self.REDIRECTED_URI
#         }
#         return requests.get(reverse(self._get_url(self._get_url_param(self.ROUTS["get_token"]), True), query=params))
    
    
#     def refreshing_user_access_token(self, user_refresh_token):
#         params = {
#         "client_id": self.CLIENT_ID,
#         "client_secret": self.CLIENT_SECRET,
#         "grant_type": "refresh_token",
#         "refresh_token": user_refresh_token,
#         "scope": ""
#         }
#         return requests.post(reverse(self._get_url(self._get_url_param(self.ROUTS["get_token"]), True), query=params))

    
#     def requesting_user_info(self, user_access_token):
#         headers = {"Authorization": f"Bearer {user_access_token}"}
#         return requests.get(reverse(self._get_url(self._get_url_param(self.ROUTS["user_info"]), True), headers=headers))
    
    
    # def get_characters(self): # demo api
    #     headers = {"Authorization": f"Bearer {self.DEMO_USER_TOKEN}"}
    #     response = requests.get(self._get_url(self._get_url_param(self.ROUTS["characters"]), False), headers=headers)
    #     return response