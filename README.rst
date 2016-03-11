Jaguares
==============================

git - github
Trello
python
django
javascript
css


LICENSE: GPLv3

Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html







It's time to write the code!!!


Running end to end integration tests
------------------------------------

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the jaguares/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.


Deployment
----------

We providing tools and instructions for deploying using Docker and Heroku.

Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html


## Historias de Usuario

0. Como administrador del proyecto me gustaría poder crear un proyecto con Sprints tal que pueda registrar el inicio, duración, comentarios y documentos adjuntos
1. Como administrador del proyecto me gustaría poder crear Historias de usuario dentro de un Sprint
2. Como Administrador del proyecto me gustaría crear tareas para cumplir una Historia de Usuario.
3. Como administrador de proyecto quisiera poder agregar miembros a un equipo de trabajo
4. Como miembro de un Proyecto me gustaría poder visualizar las tareas en un Tablero de trabajo (ToDo, Doing y Done).

## Criterios de Aceptación

### H0
- Debo poder crear un proyecto con al menos un sprint
- Debo poder crear un sprint con fecha de inicio
- Debo poder crear un sprint con duración de la misma
- Debo poder crear un sprint con descripción 
- Debo poder crear un sprint junto la opción de agregar Documentos Adjuntos
- debo poder editar los datos del Sprint.

### H1
- Debo poder crear una historia de usuario en una lista Backlog.
- Debo poder crear una historia de usuario con un Id único, nombre, descripción, criterios de aceptación y prioridad.
- Debo poder asignar una HU a un Sprint
-Debo poder ver las Historias de Usuario ordenadas por Prioridad 

### H2
- Debo poder crear una tarea con estado inicia "toDo"
- Debo poder crear una Tarea con Id único, Id de la HU a la que pertenece, Nombre, complejidad, dueño, fecha inicio, fecha fin y su estado.
- Debo poder crear una tarea desde una HU.
- Debo poder modificar el estado de una tarea creada (toDo, doing, done)
- Debo poder modificar una tarea para actualizar la fecha de inicio estimada
- Debo poder modificar una tarea para actualizar la fecha de fin estimada

### H3
- Seleccionar a un miembro de los usuarios del sistema para agregarlo a un Proyecto.
- Debo poder dar de baja a un miembro del Proyecto.
- Debo poder asignar un Rol a un miembro del Proyecto.
- Debo poder cambiar un Rol a un miembro del Proyecto.

### H4
- Solo los miembros del Proyecto podrán ver el Tablero simple.
- Las Tareas creadas deben poder verse en el Tablero.
- Debo poder mover una tarea a las diferentes columnas del Tablero, cambiando el estado de esa tarea.

# Help Commands(Ayuda)
```bash

source ~/django/bin/activate

django-admin startproject proyecto
```

##deploy:
```bash
./manage.py runserver
```

## **crear la base de datos**
para migrations data base:

mc (como total comander)


- `./manage.py makemigrations`
- `./manage.py migrate`
- `./manage.py loaddata datos`
- `./manage.py createsuperuser`
- `./manage.py loaddata ejemplo`

borrar db: `rm db.sqlte3`
borrar migrations:
proyectos/migrations: `rm 0001/initial.py ` todos los *.py excepto __init__.py

en caso de borrar todo excepto .git

`git reset --hard HEAD`


sino:
git clone https://github.com/danielstp/jaguares.git


instaladores
`pip install -r requirements.txt`

para ambiente de desarrollo
`pip install -r requirements/local.txt`

borrar db: `rm db.sqlte3`
borrar migrations:
proyrctos/migrations: `rm 0001/initial.py`  ... etc.

## Crear los datos de Ejemplo
- `./manage.py dumpdata -e auth.user --indent 2 -e auth.permission -e proyecto.estado -e contenttypes.contenttype -e proyecto.prioridad -e sessions.session -e admin.logentry -e proyecto.rol > proyecto/fixtures/ejemplo.json`
