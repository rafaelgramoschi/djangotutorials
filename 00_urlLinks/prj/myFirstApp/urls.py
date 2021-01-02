#we need to create this file because it doesn't exist

#we import those used functions and files

from django.urls import path
from . import views

#we set this variable as in the main urls.py file
urlpatterns = [
	#we indicate the url path to this "home" page,
	#and the function that will be called (views.py)
    path('', views.home, name='home'),
]