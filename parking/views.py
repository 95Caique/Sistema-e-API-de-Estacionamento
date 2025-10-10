from rest_framework.permissions import IsAdminUser, DjangoModelPermissions

from rest_framework import viewsets

from core.permissions import IsOwnerOfVehicleOrRegister
from parking.models import ParkingRecord, ParkinSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkinSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]



class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRegister]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
