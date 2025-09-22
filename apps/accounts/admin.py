from django.contrib import admin
from .models import EXBOUser


@admin.register(EXBOUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user_id", "access_token", "token_expires_in"]
