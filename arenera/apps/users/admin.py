""" User Admin """

#Django
from django.contrib import admin

#Apps
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','category')



