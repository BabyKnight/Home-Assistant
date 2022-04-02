from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
		#return HttpResponse("Welocme Home!")
		template_name = 'welcome.html'
		return render(request, template_name)

def portal(request, lang='en'):
		return HttpResponse("[%s] Welcome Home! This is The portal page of Home-Assistant" % lang)

def login(request):
		print(request.method)
		template_name = 'login.html'
		return render(request, template_name)
