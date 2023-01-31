from django.shortcuts import render
from django.http import HttpResponse

def house(request):
	return HttpResponse("House page!")
	#template_name = 'welcome.html'
	#return render(request, template_name)
