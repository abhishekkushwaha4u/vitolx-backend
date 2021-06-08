from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from chat.models import (
    Message
)
from chat.serializers import (
    MessageCreateSerializer,
    UnreadMessageSerializer
)
from chat.permissions import BlockRoomPermission
from django.db.models import Q

User = get_user_model()


class MessageCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, receiver=User.objects.get(email=self.request.data.get('receiver')))

class GetUnreadChatView(ListAPIView):
    permission_classes = [IsAuthenticated, BlockRoomPermission]
    serializer_class = UnreadMessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        output = Message.objects.filter(
            Q(sender=self.request.user, receiver__email=self.request.query_params.get('user2')) | Q(
                receiver=self.request.user, sender__email=self.request.query_params.get('user2')
                )).exclude(is_read=False)
        print(output)
        output.update(is_read=True)
        return output
