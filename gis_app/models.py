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




class ParcelDemography(models.Model):
    parcel_id = models.UUIDField(primary_key=True)
    data_class = models.CharField(max_length=100)
    parcel_name = models.CharField(max_length=100)
    sub_area_id = models.CharField(max_length=100)
    address_details_visibility = models.BooleanField(default=False)
    address_type = models.CharField(max_length=100)
    address_prefix = models.CharField(max_length=50, null=True, blank=True)
    address_number = models.CharField(max_length=50)
    address_suffix = models.CharField(max_length=50, null=True, blank=True)
    street_id = models.CharField(max_length=100)
    address_description = models.CharField(max_length=255)
    parcel_reference_name = models.CharField(max_length=100)
    corner_piece_parcel = models.BooleanField(default=False)
    adjoining_street_id = models.CharField(max_length=100, null=True, blank=True)
    parcel_length = models.FloatField()
    parcel_width = models.FloatField()
    parcel_status = models.CharField(max_length=100)
    parcel_type = models.CharField(max_length=100)
    estate_name = models.CharField(max_length=100, null=True, blank=True)
    parcel_fence_presence = models.BooleanField(default=False)
    fence_material = models.CharField(max_length=100, null=True, blank=True)
    fence_height = models.CharField(max_length=100)
    parcel_edge_structure_presence = models.BooleanField(default=False)
    parcel_edge_structure_type = models.CharField(max_length=100, null=True, blank=True)
    parcel_edge_structure_location = models.CharField(max_length=100, null=True, blank=True)
    gate_presence = models.BooleanField(default=False)
    number_of_gates = models.IntegerField(null=True, blank=True)
    gate_position = models.CharField(max_length=100, null=True, blank=True)
    number_of_homes = models.IntegerField(null=True, blank=True)
    projected_homes = models.IntegerField(null=True, blank=True)
    ipnx_connectivity_status = models.CharField(max_length=100)
    number_of_connected_homes = models.IntegerField(null=True, blank=True)
    mst_id = models.CharField(max_length=100)
    infrastructure_presence = models.BooleanField(default=False)
    visible_infrastructure = models.CharField(max_length=255, null=True, blank=True)
    setback_presence = models.BooleanField(default=False)
    setback_type = models.CharField(max_length=100, null=True, blank=True)
    setback_surface_type = models.CharField(max_length=100, null=True, blank=True)
    setback_soil_type = models.CharField(max_length=100, null=True, blank=True)
    length_asphalt = models.FloatField(null=True, blank=True)
    length_bushy = models.FloatField(null=True, blank=True)
    length_concrete = models.FloatField(null=True, blank=True)
    length_flowerbed = models.FloatField(null=True, blank=True)
    length_interlock = models.FloatField(null=True, blank=True)
    length_lawn = models.FloatField(null=True, blank=True)
    length_marble_tiles = models.FloatField(null=True, blank=True)
    length_soil = models.FloatField(null=True, blank=True)
    length_others = models.FloatField(null=True, blank=True)
    setback_structure_presence = models.BooleanField(default=False)
    setback_structure_type = models.CharField(max_length=100, null=True, blank=True)
    setback_width = models.FloatField(null=True, blank=True)
    setback_structure_location = models.CharField(max_length=100, null=True, blank=True)
    road_name = models.CharField(max_length=100)
    road_class = models.CharField(max_length=100)
    road_surface = models.CharField(max_length=100)
    road_direction = models.CharField(max_length=100)
    road_condition = models.CharField(max_length=100)
    number_of_lanes = models.IntegerField()
    pedestrian_walkway_presence = models.BooleanField(default=False)
    pedestrian_walkway_surface = models.CharField(max_length=100, null=True, blank=True)
    pedestrian_walkway_surface_widt = models.FloatField(null=True, blank=True)
    drainage_presence = models.BooleanField(default=False)
    drainage_type = models.CharField(max_length=100, null=True, blank=True)
    drainage_condition = models.CharField(max_length=100, null=True, blank=True)
    drainage_flow_type = models.CharField(max_length=100, null=True, blank=True)
    drainage_width = models.FloatField(null=True, blank=True)
    drainage_depth = models.FloatField(null=True, blank=True)
    road_to_drainage_setback_availa = models.BooleanField(default=False)
    drainage_wall_type = models.CharField(max_length=100, null=True, blank=True)
    drainage_wall_type_condition = models.CharField(max_length=100, null=True, blank=True)
    drainage_cover_presence = models.BooleanField(default=False)
    drainage_cover_type = models.CharField(max_length=100, null=True, blank=True)
    device_model = models.CharField(max_length=100, null=True, blank=True)
    drainage_cover_length = models.FloatField(null=True, blank=True)
    drainage_cover_thickness = models.FloatField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    project_id = models.CharField(max_length=100)
    cabinet_area = models.CharField(max_length=100)
    captured_by = models.CharField(max_length=100)
    captured_on = models.DateTimeField()
    # objecteid = models.CharField(max_length=100)
    createdby = models.CharField(max_length=100)
    createdat = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=100, null=True, blank=True)
    editedat = models.DateTimeField(null=True, blank=True)
    geom = models.PolygonField(srid=4326)

    class Meta:
        managed = False  # No migrations for existing table
        db_table = 'parcel_demography'  # Name of the existing table in the database

    def __str__(self):
        return self.parcel_name

class FeederCable(models.Model):
    cable_id = models.UUIDField(primary_key=True)
    cable_run_no = models.CharField(max_length=100)
    span_id = models.CharField(max_length=100)
    segment_length = models.FloatField()
    structure_a_slack_length = models.FloatField(null=True, blank=True)
    structure_b_slack_length = models.FloatField(null=True, blank=True)
    structure_a_slack_number_of_turns = models.IntegerField(null=True, blank=True)
    structure_b_slack_number_of_turns = models.IntegerField(null=True, blank=True)
    project_id = models.CharField(max_length=100)
    cabinet_area = models.CharField(max_length=100)
    # objecteid = models.BooleanField(default=False)
    createdby = models.CharField(max_length=100)
    createdat = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=100, null=True, blank=True)
    editedat = models.DateTimeField(null=True, blank=True)
    geom = models.LineStringField(srid=4326)  # Use LineStringField for cable paths
    duct_no = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False  # No migrations for existing table
        db_table = 'feeder_cable'  # Name of the existing table in the database

    def __str__(self):
        return f"Cable {self.cable_run_no} - Span {self.span_id}"



# class LineFeature(models.Model):
#     name = models.CharField(max_length=100)
#     path = models.LineStringField(srid=4326)

#     def __str__(self):
#         return self.name


# class PolygonFeature(models.Model):
#     name = models.CharField(max_length=100)
#     area = models.PolygonField(srid=4326)

#     def __str__(self):
#         return self.name
