from django.contrib import admin
from .models import PointFeature, LineFeature, PolygonFeature

# Register the models
admin.site.register(PointFeature)
admin.site.register(LineFeature)
admin.site.register(PolygonFeature)
