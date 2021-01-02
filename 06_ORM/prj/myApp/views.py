from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
	#REMEMBER TO INCLUDE {% load static %} at the beginning of everyfile
	#AND href=" {% static 'style/css/style.css' %} "

	dest1 = Destination()
	dest1.name = "Dynamic name: Bali"
	dest1.price = 600
	dest1.desc = "Dynamic description: Nulla pretium tincidunt felis, nec."
	dest1.img = "destination_1.jpg"
	dest1.offer = False

	dest2 = Destination()
	dest2.name = "Dynamic name: Indonesia"
	dest2.price = 500
	dest2.desc = "Dynamic description: Fluid Sea."
	dest2.img = "destination_2.jpg"
	dest2.offer = True

	dest3 = Destination()
	dest3.name = "Dynamic name: San Francisco"
	dest3.price = 700
	dest3.desc = "Dynamic description: The red bridge."
	dest3.img = "destination_3.jpg"
	dest3.offer = False

	# IF we pass an object, and in the html file we say
	# {{dest1.name}},{{dest1.price}}..
	# to access the data
	# <p> The price is ... {{dest1.price}}</p>
	# return render(request, 'index.html', {'dest1':dest1})

	dests = [ dest1, dest2, dest3 ]
	# IF we pass more objects, you'll need to do this:
	return render(request, 'index.html', {'dests': dests})
