from django.db import models


class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=100, db_index=True)
    ru_name = models.CharField(max_length=255, db_index=True, blank=False)
    en_name = models.CharField(max_length=255, db_index=True, blank=False)
    icon = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, db_index=True)
    color = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    infoblocks = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        db_table = "items"
        ordering = ("en_name",)
