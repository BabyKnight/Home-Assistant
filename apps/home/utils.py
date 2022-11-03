import re
from django.contrib.auth.models import User
from home.models import UserProfile


def create_account(user_name, password, profile_detail=None):
	"""
	Method to register a user with profile to create an account
	user_name: <str>
	password: <str>

	expected profile_detail struct:
		{
			'first_name': FIRST_NAME,
			'last_name': LAST_NAME,
			'gender': GENDER,
			'birthday': BIRTHDAY,
			'address': ADDRESS,
			'email': EMAIL,
			'phone': PHONE,
		}

	Return type: int
	Return: status code (decimal value of binary flag)
			[ - 0  0  0]
			    ^  ^  ^
				f1 f2 f3
			[f1]  - is password valid, 0 for valid, 1 for invalid
			[f2]  - is user name valid, 0 for valid, 1 for invalid
			[f3]  - is user name available, 0 for avaliable, 1 for not available

			[ 0]  - account created successfully
			[-1]  - invalid user name
			[-2]  - user name not available
			[-4]  - invalid password
			[-5]  - invalid password and invalid user name
			[-6]  - invalid password an user name not available
	"""

	status_code = 0
	# verify user input
	if not is_username_valid(user_name):
		status_code += -1

	elif not is_username_available(user_name):
		status_code += -2

	if not is_password_valid(password):
		status_code += -4

	if status_code != 0:
		return status_code

	# create user
	user = User.objects.create_user(username=user_name, password=password)

	# create User Profile
	user_profile = UserProfile()
	user_profile.user = user
	user_profile.save()

	return status_code


def set_user_profile(profile_detail):
	"""
	Method to set up user profile
	"""
	pass


def is_username_valid(username):
	"""
	Method to verify username
	Valid username should less than 30 characters, Letters, digits, '-', '_' and '.' only
	Return type: bool
	Return: True/False
	"""

	# valid username length should between 1 ~ 30
	if len(username) <= 0 or len(username) > 30:
		# 'msg': 'Username cannot longger than 30 characters or empty',
		return False

	# valid username should only contain Letters, digits, "-", "_" and "."
	elif not bool(re.match("^[A-Za-z0-9._-]*$", username)):
		# 'msg': 'Valid username should only contain Letters, digits, "-", "_" and "."',
		return False

	else:
		return True


def is_username_available(username):
	"""
	Method to verify if username is available
	Return type: bool
	Return: False/True
	"""

	# valid username should be unique
	if User.objects.filter(username=username).exists():
		# 'msg': 'Username already exist',
		return False

	# available username
	else:
		return True


def is_password_valid(password):
	"""
	Method to verify password
	Valid password should no less than 6 characters
	Return type: bool
	Return: False/True
	"""
	# valid password length should between 6(6 included) ~ 30
	if len(password) < 6 or len(password) > 30:
		# 'msg': 'Password required no less than 6 characters',
		return False

	# available password
	#'msg': 'Valid password'
	return True
