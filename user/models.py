from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user.custom_user_manager import UsersManager
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full name"), max_length=255)
    active = models.BooleanField(_("active"), default=True)
    staff = models.BooleanField(_("staff"), default=False)
    admin = models.BooleanField(_("admin"), default=False)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)


    objects = UsersManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_fullname(self):
        return self.full_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileimage = models.ImageField()
    phone_number = models.CharField(max_length=15, unique=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.full_name