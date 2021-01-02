from django.db import models

# Create your models here.

#we create an object destination, in order to make the page's content dynamic
class Destination:
	id : int
	name : str
	img : str
	desc : str
	price : int
