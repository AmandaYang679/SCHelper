from django.db import models
from django.contrib.auth.models import BaseUserManager
# 1 пишу фул сама без django модуля
# 2 разбираюсь, как работает django модуль и вмешиваюсь в его работу, предусмотренную его документацией

 
class EXBOUser(models.Model):
    user_id = models.IntegerField(unique=True, null=True)
    access_token = models.TextField(blank=False, null=True)
    refresh_token = models.TextField(blank=False, null=True)
    token_expires_in = models.IntegerField(blank=False, null=True)
    
    # objects = CustomUserManager()
    def __str__(self): # Эта функция влияет на то, по какому параметру будут сортироваться users в админке
        return self.user_id

