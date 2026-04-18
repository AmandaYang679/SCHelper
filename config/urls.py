"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.accounts import views


base_dir = "api/v1/"

urlpatterns = [
    path(base_dir + "admin/", admin.site.urls),
    path(base_dir + "auth/exbo/", views.ExboAuthView.as_view(), name='exbo_auth'),
    path(base_dir + "auth/exbo/callback/", views.ExboCallbackView.as_view()),
    path(base_dir + "refresh-token/", views.ExboRefreshAccessToken.as_view(), name="refresh_access_token"),
    path(base_dir + "characters/", views.GetPlayerCharacters.as_view(), name="characters_by_region"),
    path(base_dir + "profile/", views.CharacterProfile.as_view(), name="profile"),
    path(base_dir + "emission/", views.GetPlayerEmissionStatus.as_view(), name="emission_status"),
    
    # path(base_dir + "tierlist/", include("apps.tierlist.urls")),
]
