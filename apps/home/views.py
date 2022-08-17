from django.shortcuts import render
from django.http import HttpResponse


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
				#register(request)
				status = {'msg': "Welcome Home!"}
				return render(request, template_name, status)
