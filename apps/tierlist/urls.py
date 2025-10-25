from django.urls import path
from . import views


app_name = "tierlist"
base_dir = "api/v1/"

urlpatterns = [
    path("", views.ItemListView.as_view(), name="tierlist"),
]
