from django.urls import path, re_path

from . import views

app_name = 'events'

urlpatterns = [
		path('', views.events, name='events'),
]
