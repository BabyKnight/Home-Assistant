from django.contrib import admin

from .models import House
from .models import Room
from .models import Device

# Register model to be displayed in admin page
admin.site.register(House)
admin.site.register(Room)
admin.site.register(Device)
