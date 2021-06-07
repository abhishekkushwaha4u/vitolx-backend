# -*- coding: utf-8 -*-
from .admin_forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    # Forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying User model.
    # These overried the definitions on the base UserAdmin
    # That reference specific fields on auth.User

    list_display = ("email",)
    list_filter = ("staff", "admin")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name",)}),
        ("Permission", {"fields": ("admin", "staff")}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                ),
            },
        ),
    )

    search_fields = ("email", "full_name")
    ordering = ("email", "created_at")
    filter_horizontal = ()
