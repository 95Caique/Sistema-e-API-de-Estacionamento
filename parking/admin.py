from django.contrib import admin

from parking.models import ParkinSpot, ParkingRecord


@admin.register(ParkinSpot)
class ParkinSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied']
    search_fields = ['spot_number']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_type']
    search_fields = ['vehicle__licence_plate', 'parking_spot__spot_number']

