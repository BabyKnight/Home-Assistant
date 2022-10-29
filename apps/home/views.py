from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from home.models import User_Profile
from django.core.exceptions import ObjectDoesNotExist

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
		print("Login request")
		#register(request)
		status = {'msg': "Welcome Home!"}
		return render(request, template_name, status)

def register(request):
	template_name = 'register.html'
	if request.method == 'GET':
		return render(request, template_name)

	elif request.method == 'POST':
		form_data = request.POST
		user_name = form_date.get('user_name')
		first_name = form_date.get('first_name')
		last_name = form_date.get('last_name')
		password = form_date.get('password')

		gender = form_date.get('gender')
		age = form_date.get('age')
		address = form_date.get('address')
		email = form_date.get('email')
		phone = form_date.get('phone')

		try:
			user_exist = User.objects.get(username=user_name)
		except ObjectDoesNotExist:
			print("username is already exist!")
			status = {'msg': "Username is already exist!"}

		print("register request")
		status = {'msg': "Registered!"}
		return render(request, template_name, status)

