from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from home.models import UserProfile

def welcome(request):
	#return HttpResponse("Welocme Home!")
	template_name = 'welcome.html'
	return render(request, template_name)

def home(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def login(request):
	template_name = 'login.html'
	if request.method == 'GET':
		return render(request, template_name)

	elif request.method == 'POST':
		form_data = request.POST
		user_name = form_data.get('user_name')
		password = form_data.get('password')

		try:
			user = User.objects.get(username = user_name)

			status = {
					'status_code': 0,
					'msg': "Welcome Home!",
					}
			return render(request, template_name, status)

		# if user does not exist
		except ObjectDoesNotExist:
			print("User does't not exist!")
			status = {
					'status_code': -1,
					'msg': "User name doesn't exist",
					}
			return render(request, template_name, status)


def register(request):
	template_name = 'register.html'
	if request.method == 'GET':
		reg_form = UserCreationForm()
		return render(request, template_name, {'form': reg_form})

	elif request.method == 'POST':
		form_data = request.POST
		user_name = form_data.get('user_name')
		first_name = form_data.get('first_name')
		last_name = form_data.get('last_name')
		password = form_data.get('password')

		gender = form_data.get('gender')
		birthday = form_data.get('birthday')
		address = form_data.get('address')
		email = form_data.get('email')
		phone = form_data.get('phone')

		# call UserCreationForm to ceate user
		tmp_form = {
			'username': user_name,
			'password1': password,
			'password2': password,
			}
		request_form = UserCreationForm(tmp_form)

		# return to template if the data in request form is invalid
		if not request_form.is_valid():
			reg_form = UserCreationForm()
			status = {
					'status_code': -1,
					'msg': 'Invalid User name or password'
					}
			return render(request, template_name, {'form': reg_form, 'st': status, 'msg': 'Invalid uer name or password'})

		else:
			user = request_form.save()
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.save()

			user_profile = UserProfile(user=user)
			user_profile.gender = gender
			user_profile.birthday = birthday
			user_profile.address = address
			user_profile.phone = phone
			#user_profile.login_ip = None
			user_profile.save()
			reg_form = UserCreationForm()
			status = {
					'status_code': 0,
					'msg': 'User created'
					}

			return render(request, template_name, {'form': reg_form, 'st': status})

		"""
		# Use customize method to create user, without verify username and password format
		try:
			user_exist = User.objects.get(username=user_name)
		except ObjectDoesNotExist:
			print("username is already exist!")
			status = {'msg': "Username is already exist!"}
			return render(request, template_name, {'form': reg_form})
		user = User(username=user_name, password=make_password(password))
		"""

def logout(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def profile(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def profile_update(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def password_change(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)
