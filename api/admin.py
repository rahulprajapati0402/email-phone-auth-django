from django.contrib import admin

from .models import CustomUser


# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "first_name", "last_name")
