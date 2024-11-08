
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Handhole, FeederCable, ParcelDemography
from .serializers import HandholeSerializer, LineFeatureSerializer, PolygonFeatureSerializer
from django.shortcuts import render
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .permissions import IsSuperUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # For displaying error messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to home or any other page
        else:
            messages.error(request, 'Invalid username or password.')  # Error message

    return render(request, 'gis_app/login.html')


class HandholeViewSet(viewsets.ModelViewSet):
    queryset = Handhole.objects.all()
    serializer_class = HandholeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['structure_name', 'deployment_status', 'sub_area_id']
    search_fields = ['structure_name', 'physical_address']
    ordering_fields = ['structure_name', 'createdat']
    http_method_names = ['get', 'head', 'options']
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    


class LineFeatureViewSet(viewsets.ModelViewSet):
    queryset = FeederCable.objects.all()
    serializer_class = LineFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cable_id', 'span_id']
    search_fields = ['cable_id', 'span_id']
    ordering_fields = ['cable_id', 'createdat']
    http_method_names = ['get', 'head', 'options']
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]




class PolygonFeatureViewSet(viewsets.ModelViewSet):
    queryset = ParcelDemography.objects.all()[:50]
    serializer_class = PolygonFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['parcel_name', 'sub_area_id']
    search_fields = ['parcel_name', 'physical_address']
    ordering_fields = ['parcel_name', 'createdat']
    http_method_names = ['get', 'head', 'options']
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]


def map_view(request):

    context = {
        'point_url': reverse('handhole-list'),
    }
    return render(request, 'gis_app/map.html', context)
    


