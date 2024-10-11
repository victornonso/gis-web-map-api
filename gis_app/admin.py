from django.contrib import admin
from .models import Handhole, LineFeature, PolygonFeature

# Register the models
admin.site.register(Handhole)
admin.site.register(LineFeature)
admin.site.register(PolygonFeature)
