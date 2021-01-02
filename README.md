# djangotutorials
Django how-tos

MVC - Model (data) View (html) Controller

Django works with MVT - Model View Template

why django?

1.fast programming
2.components (login, connection to db, bundled in)
3.security
4.scalability

//install python3
sudo apt-get install python3
//pkg manager
sudo apt-get install python3-pip
//install virtual environment, python3 has it already built in
sudo apt-get install python3-venv

//create new folder
mkdir project
//move into project
cd project


//----------------------------------------------------------------
//create a new folder (virtual environment with its default setup) INSIDE THE PROJECT FOLDER
python3 -m venv env

//activate environment
which python3 //shows you where python is loaded from

//from project/ type
source env/bin/activate

which python3 //should say the virtual env folder

//install django FROM project folder
pip install django //or pip3
//----------------------------------------------------------------


//now you have some django commands
django-admin //lists possible commands
//creates a new folder prova
django-admin startproject prova
//the tree will be
//project
	//env
	//prova
		//prova
			//__init__.py
			//settings.py --used for security keys, debug=true, make sure to set to false before deploying
			there are used apps (installed) listed, we can use our own apps.
			Templates, database (sqlite default), password stuff
			//urls.py --used to handle urls
			//wsgi.py --used to deploy code on test server not production
		//manage.py --used to manage project

//run the server from the folder where is manage.py
// project/prova/
python3 manage.py runserver
//you'll have the web server online

//SOOOOOo we create our first app.
//in django you make things this way
//you've got your site, which have a login(app), a payment page(another app),
and so on....

//so let's create our first app inside our project folder
//create application folder
//RUN THIS WHERE THERE IS manage.py
python3 manage.py startapp calculator

//inside calculator you have
__inti__.py
admin.py
apps.py
models.py --database
tests.py --tests
views.py --page


//----------------------------------------

//create a new file "urls.py"
//this is because so you can link this new app with a url

//inside project's urls.py link to app's urls
path('', include('calculator.urls')),
//inside app's urls.py link to view
urlpatterns[path('', views.home, name='home')]
//inside app's view, def function(request) & return HttpResponse("Hello!")

//----------------------------------------

D T L Django Template Language
you can create a page externally or with templates,
django helps building dynamic data inside static pages

//create new folder inside prova folder called
templates. we will store here all the pages

//inside project (main)'s settings we modify 'DIRS':[] entry, so django knows where they are all
'DIRS':[ os.path.join(BASE_DIR,'templates') ]
here we specify the base directory (project0)
and the folder/path containing the templates

//now go to app's view and change HttpResponse into
//render() render it's used to give a page

//-----------------------------------------

DYNAMIC CONTENT
see the html file + views.py ("{{ }}")

//-----------------------------------------
