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
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView


base_dir = "api/v1/"

urlpatterns = [
    path(base_dir + "admin/", admin.site.urls),
    path(base_dir + "auth/exbo/", views.ExboAuthView.as_view(), name='exbo-auth'),
    path(base_dir + "auth/exbo/callback/", views.ExboCallbackView.as_view()),
    path(base_dir + "token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(base_dir + "token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path(base_dir + "token/verify/", TokenVerifyView.as_view(), name='token_verify'),
    path(base_dir + "tierlist/", include("apps.tierlist.urls")),
]
