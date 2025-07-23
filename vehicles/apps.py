from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'
    verbose_name = 'Veículo'
    verbose_name_plural = 'Veículos'