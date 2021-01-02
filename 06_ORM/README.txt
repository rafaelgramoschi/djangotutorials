####### O R M ########
Object Relational Mapper
we have DATA and APPLICATION

as a user you want to interact with a DB,
we need an Application to do so

Database (relational)
tables, with attributes
Customer table, with id, name, address, phonenumber

Application
have a class Customer, with 4 fields (same as above)

we use SQL to populate
BUT
Django will create automatically tables based
on class name (table name), 4 attributes (4 columns)
the more object you create, the more rows

ORM for:
Python - Django
Java - Hibernate

creates table based on classes,
creates data based on object.

########## POSTGRES and PgAdmin Setup ##########

install PostgreSQL, which is the DBMS

# Python2
    sudo apt-get update
    sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
# Python3
    sudo apt-get update
    sudo apt-get install postgresql-10 libpq-dev pgadmin3

By default, Postgres uses an authentication scheme called "peer authentication" for local connections.
Basically, this means that if the user's operating system username matches a valid Postgres username,
that user can login with no further authentication.

We can use sudo and pass in the username with the -u option.

# Login into postgres admin account
sudo -u postgres psql

# Create Database, each project with separate db,
# for security reasons

postgres=# CREATE DATABASE myFirst_db;
CREATE USER username WITH PASSWORD 'pass';

# We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to "read committed", which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django projects will be set to use UTC. These are all recommendations from the Django project itself.

postgres=# ALTER ROLE username SET client_encoding TO 'utf-8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myFirst_db TO username;
# exit postgres
\q

install PgAdmin, which is the UI to work with user interface

################ settings.py #########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myFirst_db',
        'USER': 'username',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ALLOWED_HOSTS... it is recommended to add those IP/hosts here

############### migrate #######################

# enter virtual environment
# psycopg2 is the connector between Python and PostgreSQL
# otherwise it won't work

pip install django psycopg2
python manage.py makemigrations //sets up database structure
python manage.py migrate // migrates those setups to the postgres database

# create administrative account
python manage.py createsuperuser
# you will be asked to create a username, password and email

# remember to open the firewall's port if you're on a server