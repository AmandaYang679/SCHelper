from django.db import models


class Item(models.Model):
    id = models.CharField(primary_key=True, unique=True, db_index=True)
    
    class Meta:
        db_table = "items_id"
        ordering = ("id",)
        