from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
    

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    password = models.CharField(validators=[validate_password])
    
    exbo_user_id = models.CharField(max_length=255, null=True, blank=True)
    exbo_username = models.CharField(max_length=255, null=True, blank=True)

    exbo_access_token = models.TextField(null=True, blank=True)
    exbo_refresh_token = models.TextField(null=True, blank=True)
    exbo_token_expires_at = models.DateTimeField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)

    
    
    
    def __str__(self): # Эта функция влияет на то, по какому параметру будут сортироваться users в админке
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
