from django.urls import path, re_path

from . import views

urlpatterns = [
		path('', views.welcome, name='welcome'),
		path('home/', views.home, name='home'),
		re_path(r'^home/(?P<lang>\w+)/$', views.home, name='home'),
		path('login/', views.login, name='login'),
]
