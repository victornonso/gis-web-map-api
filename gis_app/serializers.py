from rest_framework import serializers
from .models import Handhole, FeederCable, ParcelDemography
from django.contrib.gis.geos import Point, LineString, Polygon

class HandholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handhole
        fields = '__all__'

    def create(self, validated_data):
        if 'latitude' in validated_data and 'longitude' in validated_data:
            point = Point(validated_data['longitude'], validated_data['latitude'], srid=4326)
            validated_data['geom'] = point
        return super().create(validated_data)


class LineFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederCable
        fields = '__all__'

    def create(self, validated_data):
        if 'path' in validated_data:
            line_data = validated_data.pop('path')
            line = LineString([(point['x'], point['y']) for point in line_data])
            validated_data['path'] = line
        return super().create(validated_data)


class PolygonFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelDemography
        fields = '__all__'

    def create(self, validated_data):
        if 'area' in validated_data:
            polygon_data = validated_data.pop('area')
            polygon = Polygon([(point['x'], point['y']) for point in polygon_data])
            validated_data['area'] = polygon
        return super().create(validated_data)
