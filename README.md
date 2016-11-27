# CRUD-DJANGO

### EMPEZANDO CON UN CRUD EN DJANGO

Para el desarrollo de este crud se utilizo:

* python 3.5.2
* django 1.10.3
* psycopg2 2.6.2
* postgres 9.5.3

Para la instalación primero crear una base de datos en postgres y luego asignar en el archivo refugio/settings.py

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'basededatoscreada',
            'USER': 'usuario',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 5432,
	    }
	}

Una vez configurada la base de datos nos situamos en la raiz del proyecto y ejecutamos:

	python manage.py makemigrations

	python manage.py migrate

Esos comandos crearan las tablas dentro la base de datos.
Luego corremos el servidor:

	python manage.py runserver

Si todo salio bien podremos verlo en nuestro navegador

	https://localhost:8000


