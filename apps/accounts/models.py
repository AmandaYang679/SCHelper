from django.db import models
from django.contrib.auth.models import BaseUserManager
# 1 пишу фул сама без django модуля
# 2 разбираюсь, как работает django модуль и вмешиваюсь в его работу, предусмотренную его документацией

 
class EXBOUser(models.Model):
    user_id = models.IntegerField(unique=True, null=True)
    access_token = models.TextField(blank=False, null=True)
    refresh_token = models.TextField(blank=False, null=True)
    token_expires_in = models.IntegerField(blank=False, null=True)
    
    class Meta:
        db_table = 'users'
        ordering = ('user_id',)
