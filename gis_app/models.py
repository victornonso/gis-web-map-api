from django.db import models
# Create your models here.
from django.contrib.gis.db import models

class PointFeature(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    def __str__(self):
        return self.name

class LineFeature(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField(srid=4326)
    def __str__(self):
        return self.name

class PolygonFeature(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField(srid=4326)  # Specify the spatial reference system (SRID)

    def __str__(self):
        return self.name