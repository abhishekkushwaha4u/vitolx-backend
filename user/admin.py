from django.contrib import admin

from django.contrib import admin
from .models import User, UserProfile, UserNotification
from .custom_admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(UserProfile)
admin.site.register(UserNotification)