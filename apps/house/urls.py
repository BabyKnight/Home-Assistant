from django.urls import path, re_path

from . import views

app_name = 'house'

urlpatterns = [
		path('', views.house, name='house'),
		re_path(r'^room/$', views.house, name='room'),
]
