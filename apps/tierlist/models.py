from django.db import models


class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=100, db_index=True)
    name = models.CharField(max_length=255, db_index=True, blank=False)
    icon = models.URLField(blank=True)
    category = models.CharField(max_length=100, db_index=True)
    rarity = models.CharField(max_length=50, db_index=True)
    type = models.CharField(max_length=100, db_index=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    status_state = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.TextField(blank=True, null=True)
    name_en = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    last_update = models.DateTimeField(blank=True, null=True)
    
    
    class Meta:
        db_table = 'items'
        ordering = ('name',)
