from django.contrib.gis.db import models
from django.utils.timezone import now

from django.contrib.gis.db import models

class Handhole(models.Model):
    structure_id = models.UUIDField(primary_key=True)
    structure_name = models.CharField(max_length=100)
    sub_area_id = models.CharField()
    street_id = models.CharField()
    physical_address = models.CharField(max_length=255)
    structure_placement = models.CharField(max_length=100)
    handhole_material = models.CharField(max_length=100)
    handhole_dimension = models.CharField(max_length=100)
    handhole_wall_thickness = models.FloatField(max_length=100)
    handhole_cover_type = models.CharField(max_length=100)
    handhole_cover_shape = models.CharField(max_length=100)
    handhole_cover_thickness = models.CharField(max_length=100)
    cover_seal_type = models.CharField(max_length=100)
    deployment_status = models.CharField(max_length=50)
    design_approval = models.CharField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cabinet_area = models.CharField(max_length=100)
    project_id = models.CharField()
    # objecteid = models.BooleanField(default=False)
    createdby = models.CharField(max_length=100)
    createdat = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=100, null=True, blank=True)
    editedat = models.DateTimeField(null=True, blank=True)
    geom = models.PointField(srid=4326)  # Adjust the SRID if necessary

    class Meta:
        managed = False  # Tell Django not to manage the table (no migrations)
        db_table = 'handhole'  # Specify the existing table name
        

    def __str__(self):
        return self.structure_name


class LineFeature(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField(srid=4326)

    def __str__(self):
        return self.name


class PolygonFeature(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField(srid=4326)

    def __str__(self):
        return self.name
