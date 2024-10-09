from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PointFeatureViewSet, LineFeatureViewSet, PolygonFeatureViewSet, map_view

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'points', PointFeatureViewSet)
router.register(r'lines', LineFeatureViewSet)
router.register(r'polygons', PolygonFeatureViewSet)

# Include the router's URLs in the app's URL configuration
urlpatterns = [
    path('', include(router.urls)),  # This registers the /points/, /lines/, and /polygons/ endpoints
    path('map/', map_view, name='map_view'),  # Registering the /map/ endpoint
    path('map/points/', PointFeatureViewSet.as_view({'get': 'list', 'post': 'create'}), name='map_points'),  # Adding /map/points/ endpoint
]
