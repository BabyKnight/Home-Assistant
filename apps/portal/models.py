from django.db import models

# Create your models here.

class User(models.Model):
		"""
		Class definition of User
		"""
		GENDER_CHOICES = [
				('M', 'Male'),
				('F', 'Female'),
				('U', 'Unknown'),
		]

		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)
		age = models.IntegerField(null=True, blank=True)
		gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
		address = models.CharField(null=True, blank=True, max_length=50)
		email = models.EmailField(null=True, blank=True)
		phone = models.CharField(null=True, blank=True, max_length=11)
		is_superuser = models.BooleanField(default=False)
		create_date = models.DateTimeField(auto_now_add=True)
		last_login = models.DateField(null=True, blank=True)
		login_ip = models.GenericIPAddressField(null=True, blank=True)
