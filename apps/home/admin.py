from django.contrib import admin

from .models import UserProfile

# Register UserProfile model to be displayed in admin page
admin.site.register(UserProfile)
