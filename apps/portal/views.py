from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
		return HttpResponse("Welocme Home!")

def portal(request, lang='en'):
		return HttpResponse("[{}] Welcome Home! This is The portal page of Home-Assistant".format(lang))

def login(request):
		return HttpResponse("Login page")
