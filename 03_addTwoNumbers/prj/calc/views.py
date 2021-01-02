from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def add(request):
	val1 = int(request.GET['numa'])
	val2 = int(request.GET['numb'])

	res = val1 + val2

	return render(request, 'result.html', {'result':res})
