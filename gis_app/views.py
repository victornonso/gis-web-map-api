# from django.shortcuts import render
# from django.urls import reverse

# # Create your views here.

# from rest_framework import viewsets
# from .models import PointFeature, LineFeature, PolygonFeature
# from .serializers import PointFeatureSerializer, LineFeatureSerializer, PolygonFeatureSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
# from django.shortcuts import render

# class PointFeatureViewSet(viewsets.ModelViewSet):
#     queryset = PointFeature.objects.all()
#     serializer_class = PointFeatureSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']
#     ordering_fields = ['name']


# class LineFeatureViewSet(viewsets.ModelViewSet):
#     queryset = LineFeature.objects.all()
#     serializer_class = LineFeatureSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']
#     ordering_fields = ['name']

# class PolygonFeatureViewSet(viewsets.ModelViewSet):
#     queryset = PolygonFeature.objects.all()
#     serializer_class = PolygonFeatureSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']
#     ordering_fields = ['name']


# def map_view(request):
#     print("Map view called")  # Debugging print statement
#     context = {
#         'api_points_url': reverse('pointfeature-list'),
#         'api_lines_url': reverse('linefeature-list'),
#         'api_polygons_url': reverse('polygonfeature-list'),
#     }
#     return render(request, 'gis_app/map.html', context)


from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Handhole, LineFeature, PolygonFeature
from .serializers import HandholeSerializer, LineFeatureSerializer, PolygonFeatureSerializer
from django.shortcuts import render
from django.urls import reverse

class HandholeViewSet(viewsets.ModelViewSet):
    queryset = Handhole.objects.all()
    serializer_class = HandholeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['structure_name', 'deployment_status', 'sub_area_id']
    search_fields = ['structure_name', 'physical_address']
    ordering_fields = ['structure_name', 'createdat']
    http_method_names = ['get', 'head', 'options']
    


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
    context = {
        'point_url': reverse('handhole-list'),
        'api_lines_url': reverse('linefeature-list'),
        'api_polygons_url': reverse('polygonfeature-list'),
    }
    return render(request, 'gis_app/map.html', context)

