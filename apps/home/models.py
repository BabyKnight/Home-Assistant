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

		user_name = models.CharField(max_length=30, unique=True)
		password = models.CharField(max_length=128)
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)
		age = models.IntegerField(null=True, blank=True)
		# birthday
		gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
		address = models.CharField(null=True, blank=True, max_length=50)
		email = models.EmailField(null=True, blank=True, max_length=50)
		phone = models.CharField(null=True, blank=True, max_length=11)
		is_superuser = models.BooleanField(default=False)
		is_active = models.BooleanField(default=True)
		registered_date = models.DateTimeField(auto_now_add=True)
		last_login = models.DateField(null=True, blank=True)
		login_ip = models.GenericIPAddressField(null=True, blank=True)

		@property
		def full_name(self):
				# The user is identified by user name or email address
				return "{} {}".format(self.first_name, self.last_name)


		def create_user(self, user_name, password, first_name, last_name,
						age=None, gender='U', address=None, emaili=None, phone=None,
						is_superuser=False, login_ip=None):
				"""
				Function to create user
				return: {function_call_status: msg}
				"""
				user = User(
								user_name=user_name,
								password=password,
								first_name=first_name,
								last_name=last_name,
								age=age,
								gender=gender,
								address=address,
								email=email,
								phone=phone,
								is_superuser=is_superuser,
								is_active=True,
								login_ip=login_ip,
								)
				user.save()

