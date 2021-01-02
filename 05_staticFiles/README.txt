################# settings.py #####################

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'myApplication/staticfiles/')
]

# we now join our staticfiles folder with the base root,
# django creates the folder assets in the root path  
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

############## urls.py (project) ##################

path('', include('staticFiles.urls') ),

############### urls.py (myApp) ###################

urlpatterns = [	path('', views.index, name='index'), ]

################# views.py ########################

Cretate object(s) and pass as array of objects

################# ALL HTML files ##################

# must include {{% load static %}} at the very 
# beginning of the file

# links hrefs must have {% static 'path/style.css' %}
# around them, otherwise won't work

# use jinja notation for dynamic content
# {{myObject.attribute}}

# use jinja notation for more passed objects
# {% for dest in dests %} ##dests has been passed from views.py
# {% endfor %}

# troubles with imgs?
# <img src="{% static 'path/img/{{passedObject.img}}' %}">
# won't work because html can't parse {{ }}
# SOLUTION:
# add {% static "images" as BaseImgURL %} after {% load static %}
# this will link the "images" folder's path to the variable BaseImgURL
# change your code to:
# <img src="{{BaseImgURL}}/{{passedObject.img}}">

# use IF to display special offers or not!
# {% if something %} {% endif %}

# This is how to make dynamic content