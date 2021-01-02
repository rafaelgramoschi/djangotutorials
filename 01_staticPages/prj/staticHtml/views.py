from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	#we use render to return static pages
	#we render the request and the requested page .html
	#the html page will be searched based on
	#the main settings.py file, so we create a folder templates
	#in the main project's folder and we link that folder to
	#'DIRS':[] under TEMPLATES inside settings.py
	return render(request, 'home.html')