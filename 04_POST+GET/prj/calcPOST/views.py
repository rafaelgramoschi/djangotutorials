from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def add(request):

	val1 = int(request.POST['numa'])
	val2 = int(request.POST['numb'])

	return render(request, 'result.html', {'result':val1+val2})