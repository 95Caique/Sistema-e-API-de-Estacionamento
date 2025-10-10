from rest_framework import permissions

class IsOwnerOfVehicleOrRegister(permissions.BasePermission):


    def has_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user

        if hasattr(obj, 'vehicle',) and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.user == user

        return False