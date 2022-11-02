import re
from django.contrib.auth.models import User


class User_Info():
	"""
	Struct for User info basic fields which is required while creating a user
	attributes include user_name and password
	user_name: A valid username should less than 30 characters, Letters, digits, '-', '_' and '.' only
	password: A valid password length should between 6(6 included) ~ 30(30 included), any characters
	"""
	user_name = None
	password = None
	is_valid = False

	def __init__(self, user_info_dict):
		"""
		Initializes a user info instance with a dict
		"""
		# if argument is not even a dict type
		# then initializes a user info instance without any value
		if not isinstance(user_info_dict):
			print("Argument for User info initializes is not an <dict> type!")
			pass
		else:
			self.user_name = user_info_dict.get('user_name')
			self.password = user_info_dict.get('password')

	def is_user_name_valid(self):
		res = is_username_valid(self.user_name)
		return res.get('status')

	def is_password_valid(self):
		res = is_password_valid(self.password)
		return res.get('status')


class Profile_Detail():
	pass

def user_registration(user_info, profile_detail=None):
	"""
	Method to register a user with profile

	Expected user_info struct:
		{
			'user_name': USERNAME,
			'password': PASSWORD,
		}
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

	Return type: dict
	Return: {'status': bool, 'msg': str}
	"""

	# verify user input
	is_username_valid(user_info.get('user_name'))
	is_password_valid(user_info.get('password'))

	user = User.objects.create_user(user_info.get('user_name'), user_info.get('password'))

	# create User Profile
	user_profile = User_Profile()
	user_profile.user = user
	user_profile.save()



def set_user_profile(profile_detail):
	"""
	Method to set up user profile
	"""
	pass


def is_username_valid(username):
	"""
	Method to verify username
	Valid username should less than 30 characters, Letters, digits, '-', '_' and '.' only
	Return type: dict
	Return: {'status': bool, 'msg': str}
	"""

	# valid username length should between 1 ~ 30
	if len(username) <= 0 or len(username) > 30:
		res = {
				'status': False,
				'msg': 'Username cannot longger than 30 characters or empty',
				}
		return res

	# valid username should only contain Letters, digits, "-", "_" and "."
	if not bool(re.match("^[A-Za-z0-9._-]*$", username)):
		res = {
				'status': False,
				'msg': 'Valid username should only contain Letters, digits, "-", "_" and "."',
				}
		return res	

	# valid username should be unique
	if User.objects.filter(username=username).exists():
		res = {
				'status': False,
				'msg': 'Username already exist',
				}
		return res

	# available username
	res = {
			'status': True,
			'msg': 'username is available'
			}
	return res


def is_password_valid(password):
	"""
	Method to verify password
	Valid password should no less than 6 characters
	Return type: dict
	Return: {'status': bool, 'msg': str}
	"""
	# valid password length should between 6(6 included) ~ 30
	if len(username) < 6 or len(username) > 30:
		res = {
				'status': False,
				'msg': 'Password required no less than 6 characters',
				}
		return res

	# available password
	res = {
			'status': True,
			'msg': 'Valid password'
			}
	return res
