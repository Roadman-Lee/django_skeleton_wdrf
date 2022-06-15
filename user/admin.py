from django.contrib import admin

from user.models import User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "join_date")
    list_display_links = ("username", "email", "join_date")
    list_filter = ("join_date",)
    search_fields = ("username", "email", "join_date")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "fullname",
        "nickname",
        "zipcode",
        "address",
        "introduction",
        "birthday",
    )
    list_display_links = (
        "fullname",
        "nickname",
        "zipcode",
        "address",
        "introduction",
        "birthday",
    )
    list_filter = ("address",)
    search_fields = (
        "fullname",
        "nickname",
        "zipcode",
        "address",
        "introduction",
        "birthday",
    )
