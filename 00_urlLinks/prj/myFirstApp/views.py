from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("This is myFirstApp.<br>\
		We link the urls to get to this application page. <br><br>\
		We modify prj/urls.py<br>\
		<b>path('', include('myFirstApp.urls') ),</b><br><br>\
		We create and modify myFirstApp/urls.py.<br>\
		<b>from django.urls import path\
			<br>from . import views</b><br>\
		<b>path('', views.home, name='home'),</b><br><br>\
		We code myFirstApp/views.py to display this message.\
		<br>This is a static HttpResponse.")