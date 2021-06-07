# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.models import UserProfile
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "created_at",
            "password"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "full_name"
            "email",
            "created_at"
        ]


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name","email", "created_at"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name"]

class UserProfileCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        exclude = ["user", "id"]
        
class UserFullProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(source='userprofile.profileimage')
    phone_number = serializers.CharField(source='userprofile.phone_number')
    bio = serializers.CharField(source='userprofile.bio')
    class Meta:
        model = User
        fields = ["full_name", "email", "profile_picture", "phone_number", "bio"]



class UserProfilePictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["profileimage"]