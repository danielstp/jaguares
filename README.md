# Jaguares
Experimento de Django + Angular
- bootstrap (propuesta usar con sass)
- Angular.js
- Git
- Django
- Python


## Historia de Usuario Inicial

- Como administrador de proyecto me gustaria poder crear un proyecto con Sprints tal que pueda registar el inicio, duración, comentarios y documentos adjuntos
- Como administrador de proyecto me gustaria crear Tareas para cumplir las historias de usuario dentro del sprint

## Criterios de Aceptacion
### H1
- Debo poder crear un proyecto con al menos un sprint
- Debo poder crear un sprint con fecha de inicio
- Debo poder crear un sprint con duración de la misma
- Debo poder crear un sprint con descripción 
- Debo poder crear un sprint junto la opcion de agregar Documentos Adjuntos
- debo poder editar los datos del Sprint.

### H2
- Debo poder crear una tarea con estado inicial de BackLog
- Debo poder visualizar las tareas creadas en un tablero de tareas.
- Debo poder modificar una tarea para actualizar la fecha de inicio estimada
- Debo poder modificar una tarea para actualizar la fecha estimada de finalización

### H3
- descripcion
- 
###Help Commands
django-admin manage.py
django-admin manage.py server

source ~/django/bin/activate
deploy:
./manage.py runserver

para migrations data base:
mc (cm total comander)

- ./manage.py makemigrations
- ./manage.py migrate
-  ./manage.py loaddata datos

- ./manage.py createsuperuser

borrar db: rm db.sqlte3
borrar migrations:
proyectos/migrations: rm 0001/initial.py....etc

en caso de borrar todo excepto .git
git reset --hard HEAD
//crear la base de datos
 ./manage.py/

sino:
git clone https://github.com/danielstp/jaguares.git


instaladores
pip install -r Requiriments.txt

borrar db: rm db.sqlte3
borrar migrations:
proyrctos/migrations: rm 0001/initial.py....etc

