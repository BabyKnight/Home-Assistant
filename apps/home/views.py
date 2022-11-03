from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from home.models import UserProfile
from home.utils import create_account

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
		user_name = request.POST.get('user_name')
		password = request.POST.get('password')

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
	"""
	register view
	"""
	template_name = 'register.html'

	if request.method == 'GET':
		reg_form = UserCreationForm()
		return render(request, template_name, {'form': reg_form})

	elif request.method == 'POST':

		# required info for user registration
		user_name = request.POST['user_name']
		# password confirm should be verified in the frontend already
		password = request.POST['password']

		# aditional profile info which can be empty and updated later
		profile_detail = {
				'first_name': request.POST['first_name'],
				'last_name': request.POST['last_name'],
				'gender': request.POST['gender'],
				'birthday': request.POST['birthday'],
				'address': request.POST['address'],
				'email': request.POST['email'],
				'phone': request.POST['phone'],
				}

		res = create_account(user_name, password, profile_detail)
		reg_res = {'st': res}
		if res == 0:
			reg_res['msg'] = 'Account Created!'
		else:
			reg_res['msg'] = 'Account Create Failed with invalid input!'
		return render(request, template_name, reg_res)

def logout(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def profile(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def profile_update(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)

def password_change(request, lang='en'):
	return HttpResponse("[%s] Welcome Home! This is The home page of Home-Assistant" % lang)
