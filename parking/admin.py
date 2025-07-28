from django.contrib import admin

from parking.models import ParkinSpot, ParkingRecord


@admin.register(ParkinSpot)
class ParkinSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied']
    search_fields = ['spot_number']
    list_filter = ['is_occupied']



@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__licence_plate', 'parking_spot__spot_number']

    def formfield_for_foreignkey(self,db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkinSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
