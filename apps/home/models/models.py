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
		CATE_CHOICES = [
				('C', 'Customized'),
				('D', 'Default'),
		]
		#profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preference')
		layout = models.CharField(max_length=200, null=True, blank=True)
		theme = models.CharField(max_length=1, choices=THEME_CHOICES, default='A')
		category = models.CharField(max_length=1, choices=CATE_CHOICES, default='D')
		language = models.CharField(max_length=10, default='en')

		class Meta:
			verbose_name = 'User Preference'

		def __str__(self):
			return "<{}, {}, {} Settings>".format(
					self.id,
					self.profile.user.username,
					self.get_category_display(),
					)


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
		address = models.CharField(null=True, blank=True, max_length=50)
		avatar = models.CharField(max_length=30, blank=False, null=False, default='default_avatar.jpg')
		birthday = models.DateTimeField(null=True, blank=True)
		gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
		phone = models.CharField(null=True, blank=True, max_length=11)
		login_ip = models.GenericIPAddressField(null=True, blank=True)
		# device_list = moedls.OneToOneField(XXX, related_name='devices')
		is_at_home = models.BooleanField(null=True, blank=True)
		# will auto create a user preference config when create user profile
		preference = models.OneToOneField(UserPreference, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)

		@property
		def full_name(self):
				# The user is identified by user name or email address
				return "{} {}".format(self.user.first_name, self.user.last_name)

		def save(self, *args, **kwargs):
			"""
			Override the default save method, create UserPreference instance by default
			"""
			# auto create an user preference when create user profile, all preference keeps default
			if self.preference is None:
				preference = UserPreference()
				preference.save()
				self.preference = preference
			super(UserProfile, self).save(*args, **kwargs)

		class Meta:
			verbose_name = 'User Profile'

		def __str__(self):
			return "<{}, {}, {}>".format(
					self.user.id,
					self.user.username,
					self.full_name
					)
