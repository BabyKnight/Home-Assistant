from django.urls import path, re_path

from . import views

app_name = 'home'

urlpatterns = [
		path('', views.welcome, name='welcome'),
		re_path(r'^home/$', views.home, name='home'),
		re_path(r'^home/(?P<lang>\w+)/$', views.home, name='home'),
		re_path(r'^login/$', views.login, name='login'),
		re_path(r'^register/$', views.register, name='register'),
		re_path(r'^logout/$', views.logout, name='logout'),
		re_path(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
		re_path(r'^profile_update/(?P<pk>\d+)/$', views.register, name='profile_update'),
		re_path(r'^pwd_change/$', views.register, name='password_change'),
]
