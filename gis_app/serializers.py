# from rest_framework import serializers
# from .models import PointFeature, LineFeature, PolygonFeature  # Ensure this line is correct
# from django.contrib.gis.geos import Point, LineString, Polygon  # Import necessary classes for spatial data

# class PointFeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PointFeature
#         fields = '__all__'

#     def create(self, validated_data):
#         # Check for spatial field (assuming it's named 'location')
#         if 'location' in validated_data:
#             location_data = validated_data.pop('location')  # Extract the location data
#             # Create a Point instance (adjust keys based on your actual data structure)
#             point = Point(location_data['x'], location_data['y'])
#             validated_data['location'] = point  # Assign the Point instance back to validated_data

#         return super().create(validated_data)  # Call the parent class's create method

# class LineFeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LineFeature
#         fields = '__all__'

#     def create(self, validated_data):
#         # Check for spatial field (assuming it's named 'line_coordinates')
#         if 'line_coordinates' in validated_data:
#             line_data = validated_data.pop('line_coordinates')  # Extract the line coordinates
#             # Create a LineString instance (assuming it's a list of dictionaries with 'x' and 'y')
#             line = LineString([(point['x'], point['y']) for point in line_data])
#             validated_data['line_coordinates'] = line  # Assign the LineString instance back to validated_data

#         return super().create(validated_data)

# class PolygonFeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PolygonFeature
#         fields = '__all__'

#     def create(self, validated_data):
#         # Check for spatial field (assuming it's named 'polygon_coordinates')
#         if 'polygon_coordinates' in validated_data:
#             polygon_data = validated_data.pop('polygon_coordinates')  # Extract the polygon coordinates
#             # Create a Polygon instance (assuming it's a list of tuples or dicts with 'x' and 'y')
#             polygon = Polygon([(point['x'], point['y']) for point in polygon_data])
#             validated_data['polygon_coordinates'] = polygon  # Assign the Polygon instance back to validated_data

#         return super().create(validated_data)


from rest_framework import serializers
from .models import Handhole, LineFeature, PolygonFeature
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
        model = LineFeature
        fields = '__all__'

    def create(self, validated_data):
        if 'path' in validated_data:
            line_data = validated_data.pop('path')
            line = LineString([(point['x'], point['y']) for point in line_data])
            validated_data['path'] = line
        return super().create(validated_data)


class PolygonFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolygonFeature
        fields = '__all__'

    def create(self, validated_data):
        if 'area' in validated_data:
            polygon_data = validated_data.pop('area')
            polygon = Polygon([(point['x'], point['y']) for point in polygon_data])
            validated_data['area'] = polygon
        return super().create(validated_data)
