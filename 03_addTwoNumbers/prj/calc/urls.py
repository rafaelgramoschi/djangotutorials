from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	#how to read this:
	#when someone searches for add,
	#go to views.add
	#the name is add
	path('add', views.add, name='add')
]