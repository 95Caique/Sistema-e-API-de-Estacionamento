from rest_framework import serializers

from parking.models import ParkinSpot, ParkingRecord

class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkinSpot
        fields = '__all__'


class ParkingRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecord
        fields = '__all__'