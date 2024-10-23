from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HandholeViewSet, LineFeatureViewSet, PolygonFeatureViewSet, map_view

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'handholes', HandholeViewSet)
router.register(r'lines', LineFeatureViewSet)
router.register(r'polygons', PolygonFeatureViewSet)

# Include the router's URLs in the app's URL configuration
urlpatterns = [
    path('', include(router.urls)),  # Registers the /handholes/, /lines/, and /polygons/ endpoints
    path('map/', map_view, name='map_view'),  # Registers the /map/ endpoint
    # path('map/handholes/', HandholeViewSet.as_view({'get'}), name='map_handholes'),  # Adding /map/handholes/ endpoint
    # path('map/handholes/', HandholeViewSet.as_view({'get': 'list', 'post': 'create'}), name='map_handholes'),  # Adding /map/handholes/ endpoint
]
