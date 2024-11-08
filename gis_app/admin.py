from django.contrib import admin
from .models import Handhole, FeederCable, ParcelDemography

# Register the models
admin.site.register(Handhole)
admin.site.register(FeederCable)
admin.site.register(ParcelDemography)
