# -*- coding: utf-8 -*-
from .serializers import (
    UserReadOnlySerializer,
    UserUpdateSerializer,
    UserSerializer,
    UserProfileCreateSerializer,
    UserFullProfileSerializer,
    UserProfilePictureUpdateSerializer
)
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from user.models import (
    UserNotification
)

from django.contrib.auth import get_user_model
from user.models import UserProfile


User = get_user_model()


class CreateUserView(CreateAPIView):
    """
    Creates User Object

    Input: email, fullname, password, and profile details
    Output: User details
    Processing:
    1) Calls user model and creates the user object
    """
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
       

class CreateUserProfileView(CreateAPIView):
    """
    Creates UserProfile Object

    Input: User Profile Model objects
    Output: serialized model
    Processing:
    1) Calls userprofile model and creates the user object
    """
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        UserNotification.objects.create(user=self.request.user)

class DisplayUserFullProfileView(RetrieveAPIView):
    """
    Display User Details

    Input: Only auth token in headers
    Output: User details
    Processing:
    1) Calls user model and retrieves the user object
    """

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserFullProfileSerializer

    def get_object(self):
        return self.request.user


class UpdateUserProfilePictureView(UpdateAPIView):
    """
    Update User Profile Picture

    Input: User Profile Picture
    Output: serializer fields
    Processing:
    1) Updates the User Profile Picture Object
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfilePictureUpdateSerializer

    def get_object(self):
        return self.request.user.userprofile

class UpdateUserView(APIView):
    """
    Update User Details

    Input: User model fields and UserProfile Model Fields
    Output: serializer fields
    Processing:
    1) Fetches user model and updates the user object
    depending on serializer and userprofile model
    """
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        data1 = UserReadOnlySerializer(request.user, data=request.data, partial=True)
        data2 = UserProfileCreateSerializer(request.user.userprofile, data=request.data, partial=True)
        if data1.is_valid() and data2.is_valid():
            data1.save()
            data2.save()
            return Response({"message": "Saved Successfully"}, status=200)
        else:
            response = {"errors":[]}
            if not data1.is_valid():
                response['errors'].append(data1.errors)
            if not data2.is_valid():
                response['errors'].append(data2.errors)
            return Response(response, status=400)

class UserNotificationTokenResetView(APIView):
    def post(self, request):
        if request.data.get('key') != 'thesupersecretkey':
            return Response({"message": "Auth failed"})
        else:
            otp = request.data.get('otp', None)
            try:
                notif = UserNotification.objects.get(otp=otp)
                user_chat_id = request.data.get('chat_id')
                notif.token = user_chat_id
                notif.verified = True
                notif.save()
                return Response({"message": "User notification enabled!"})
            except Exception:
                return Response({"message": "No such otp exists"})
            
