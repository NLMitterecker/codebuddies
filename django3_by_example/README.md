# Django 3 by example - codebuddies hangout

All projects created from "Django 3 by example 3rd edition" 
(https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952).
Every chapter is stored in its own subdirectory.

## Setup environment

1) Create virtual environment to isolate installed packages from system, e.g.

~~~
$ pyton3 -m venv my_dev_env
$ . my_dev_env/bin/activate
~~~

2) Install all necessary packages within the virutal environment

~~~
pip install -r requirements.txt
~~~

## Useful django commands

The django dev server is managed through **manage.py**.

Run dev server
~~~
$ python manage.py runserver
~~~

Enter django shell
~~~
$ python manage.py shell
~~~

Synchronize new model into database
~~~
$ python manage.py makemigrations APPLICATION_NAME
~~~

Migrate new Database schema
~~~
$ python manage.py migrate
~~~

$ python manage

## dev admin account

Username and password for admin

~~~
admin/admin
~~~
