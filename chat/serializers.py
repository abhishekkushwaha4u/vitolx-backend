from rest_framework import serializers
from chat.models import Message

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["message"]

class UnreadMessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.full_name')
    class Meta:
        model = Message
        fields = ["sender", "message"]
        