# djangoapp/partners/models.py
from django.contrib.gis.db import models


class Partner(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    tradingName = models.CharField(max_length=255)
    ownerName = models.CharField(max_length=255)
    document = models.CharField(max_length=255, unique=True)
    coverageArea = models.MultiPolygonField()
    address = models.PointField()

    def __str__(self):
        return self.tradingName
