from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, this is the homepage of Vincent Site")
