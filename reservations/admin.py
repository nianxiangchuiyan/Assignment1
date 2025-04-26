from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Room, Reservation, CustomUser

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(CustomUser)
