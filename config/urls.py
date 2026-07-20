from django.contrib import admin
from django.urls import path, include
from apps.accounts import views as account_views
from apps.items_builds import views as builds_views


base_dir = "api/v1/"

urlpatterns = [
    path(base_dir + "admin/", admin.site.urls),
    path(base_dir + "auth/exbo/", account_views.ExboAuthView.as_view(), name='exbo_auth'),
    path(base_dir + "auth/exbo/callback/", account_views.ExboCallbackView.as_view()),
    path(base_dir + "auth/refresh_token/", account_views.ExboRefreshAccessToken.as_view(), name="refresh_access_token"),
    path(base_dir + "characters/", account_views.GetPlayerCharacters.as_view(), name="characters_by_region"),
    path(base_dir + "profile/", account_views.CharacterProfile.as_view(), name="profile"),
    path(base_dir + "emission/", account_views.GetPlayerEmissionStatus.as_view(), name="emission_status"),
    path(base_dir + "friends_list/", account_views.GetFriendList.as_view(), name="friends_list"),
    
    path(base_dir + "create_build/", builds_views.CreateItemsBuild.as_view(), name="create_items_build")
    # path(base_dir + "tierlist/", include("apps.tierlist.urls")),
]
