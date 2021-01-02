from django.db import models

# Create your models here.

# we create an object destination, in order to make the page's content dynamic
"""
class Destination:
	id : int
	name : str
	img : str
	desc : str
	price : int
"""

# if you want Django ORM to create table based on your object, you need
# to create that object this way->   class MyClass(models.Model):
# this will make the class inherit the feature of Model and Django will notice it

class Destination(models.Model):
	# you don't need to create id, this will be auto created.
	
	# now you can't just type in the data types, or it won't work on your db
	# google model field django reference for correct data type to write down
	name : models.CharField()

