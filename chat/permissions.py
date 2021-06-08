from rest_framework.permissions import BasePermission
from chat.models import BlockRoom

class BlockRoomPermission(BasePermission):
    def has_permission(self, request, view):
        return not (
            BlockRoom.objects.filter(
                user1=request.user, user2__email=request.query_params.get('user2')
                )|BlockRoom.objects.filter(
                    user2=request.user, user1__email=request.query_params.get('user2'))
                    )
