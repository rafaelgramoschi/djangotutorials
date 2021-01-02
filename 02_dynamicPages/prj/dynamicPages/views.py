from django.shortcuts import render

# Create your views here.

def home(request):
	#we will pass a dynamic variable to the page,
	#so the output will be dynamic.
	return render(request, 'home.html', {'name':'Rafael'})