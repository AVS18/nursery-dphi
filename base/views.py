from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import User
from customer.models import Order
from .serializers import UserSerializer,OrderSerializer,PlantSerializer
from nursery.models import Plant
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().select_related()
    serializer_class = OrderSerializer

class PlantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Plant.objects.all().select_related()
    serializer_class = PlantSerializer