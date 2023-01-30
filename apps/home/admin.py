from django.contrib import admin

from .models import UserProfile
from .models import UserPreference

# Register model to be displayed in admin page
admin.site.register(UserProfile)
admin.site.register(UserPreference)
