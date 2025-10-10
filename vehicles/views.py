from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from django.shortcuts import render
from rest_framework import viewsets

from core.permissions import IsOwnerOfVehicleOrRegister
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permissions_classes = [DjangoModelPermissions, IsAdminUser]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permissions_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRegister]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)


