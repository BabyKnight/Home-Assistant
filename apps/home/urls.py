from django.urls import path, re_path

from . import views

urlpatterns = [
		path('', views.welcome, name='welcome'),
		path('portal/', views.portal, name='portal'),
		re_path(r'^portal/(?P<lang>\w+)/$', views.portal, name='portal'),
		path('login/', views.login, name='login'),
]
