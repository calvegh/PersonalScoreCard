from django.urls import path

from . import views

urlpatterns= [

	path('', views.index, name='index'),
	path('welcome/', views.welcome, name='welcome'),
	path('info/',views.info, name='info'),
	path('contact/', views.contact, name='contact'),

	path('registrodatos/',views.registrodatos, name='registrodatos'),
	path('salud/',views.salud, name='salud')]