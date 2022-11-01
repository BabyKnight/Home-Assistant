from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class UserProfile(models.Model):
		"""
		Class definition of UserProfile
		"""
		GENDER_CHOICES = [
				('M', 'Male'),
				('F', 'Female'),
				('U', 'Unknown'),
		]

		user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
		birthday = models.DateTimeField(null=True, blank=True)
		gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
		address = models.CharField(null=True, blank=True, max_length=50)
		phone = models.CharField(null=True, blank=True, max_length=11)
		login_ip = models.GenericIPAddressField(null=True, blank=True)

		@property
		def full_name(self):
				# The user is identified by user name or email address
				return "{} {}".format(self.user.first_name, self.user.last_name)

		class Meta:
			verbose_name = 'User Profile'

		def __str__(self):
			return "{}: - {}".format(self.user.id, self.full_name)

# register UserProfile model to be displayed in admin page
admin.site.register(UserProfile)
