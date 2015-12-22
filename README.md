# Jaguares
Experimento de Django + Angular
- bootstrap (propuesta usar con sass)
- Angular.js
- Git
- Django
- Python


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
pip install -r Requirements.txt

borrar db: rm db.sqlte3
borrar migrations:
proyrctos/migrations: rm 0001/initial.py....etc

