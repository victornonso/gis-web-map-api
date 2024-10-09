from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from rest_framework import viewsets
from .models import PointFeature, LineFeature, PolygonFeature
from .serializers import PointFeatureSerializer, LineFeatureSerializer, PolygonFeatureSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render

class PointFeatureViewSet(viewsets.ModelViewSet):
    queryset = PointFeature.objects.all()
    serializer_class = PointFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class LineFeatureViewSet(viewsets.ModelViewSet):
    queryset = LineFeature.objects.all()
    serializer_class = LineFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

class PolygonFeatureViewSet(viewsets.ModelViewSet):
    queryset = PolygonFeature.objects.all()
    serializer_class = PolygonFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


def map_view(request):
    print("Map view called")  # Debugging print statement
    context = {
        'api_points_url': reverse('pointfeature-list'),
        'api_lines_url': reverse('linefeature-list'),
        'api_polygons_url': reverse('polygonfeature-list'),
    }
    return render(request, 'gis_app/map.html', context)
