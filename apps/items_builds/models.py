from django.db import models
from apps.accounts.models import EXBOUser
from apps.items_db.models import Item


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=50)
    
    class Meta:
        db_table = "tags"


class Build(models.Model):
    user = models.ForeignKey(EXBOUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    items_id = models.ManyToManyField(Item, blank=False, related_name="builds")
    tags = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        db_table = "community_builds"
        