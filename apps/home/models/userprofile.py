from django.contrib.auth.models import User
from django.db import models


class UserPreference(models.Model):
		"""
		Class definition of UserPreference
		"""
		THEME_CHOICES = [
				('D', 'Dark'),
				('L', 'Light'),
				('A', 'Auto'),
		]
		#profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preference')
		layout = models.CharField(max_length=200, null=True, blank=True)
		theme = models.CharField(max_length=1, choices=THEME_CHOICES, default='A')
		language = models.CharField(max_length=10, default='en')

		class Meta:
			verbose_name = 'User Preference'

		def __str__(self):
			#return "< {}, {} Mode, {} >".format(self.profile.full_name, self.theme.capitalize(), self.language)
			return "< {} Mode, {} >".format(self.theme.capitalize(), self.language)


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
		# device_list = moedls.OneToOneField(XXX, related_name='devices')
		is_at_home = models.BooleanField(null=True, blank=True)
		preference = models.OneToOneField(UserPreference, on_delete=models.CASCADE, related_name='profile', null=True)

		@property
		def full_name(self):
				# The user is identified by user name or email address
				return "{} {}".format(self.user.first_name, self.user.last_name)

		class Meta:
			verbose_name = 'User Profile'

		def __str__(self):
			return "{}: - {}".format(self.user.id, self.full_name)
