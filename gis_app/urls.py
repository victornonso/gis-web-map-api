from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from .views import HandholeViewSet, LineFeatureViewSet, PolygonFeatureViewSet, map_view
from . import views

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'handholes', HandholeViewSet)
router.register(r'feeder_cable', LineFeatureViewSet)   
router.register(r'parcel_demography', PolygonFeatureViewSet)

# Include the router's URLs in the app's URL configuration
urlpatterns = [
    path('', include(router.urls)),  # Registers the /handholes/, /lines/, and /polygons/ endpoints
    path('map/', map_view, name='map_view'),  # Registers the /map/ endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', views.login_view, name='login')
]