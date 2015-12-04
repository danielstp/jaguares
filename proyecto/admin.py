from django.contrib import admin

from proyecto.models import Documento
from proyecto.models import Proyecto
from proyecto.models import Miembro
from proyecto.models import Persona
from proyecto.models import HistoriaUsuario
from proyecto.models import HistoriaTarea
from proyecto.models import Tarea
from proyecto.models import Rol
from proyecto.models import CriterioAceptacion
from proyecto.models import Sprint
from proyecto.models import EstadoEmocional
from proyecto.models import Estado


admin.site.register(Documento)
admin.site.register(Proyecto)
admin.site.register(Miembro)
admin.site.register(Persona)
admin.site.register(HistoriaUsuario)
admin.site.register(HistoriaTarea)
admin.site.register(Tarea)
admin.site.register(Rol)
admin.site.register(CriterioAceptacion)
admin.site.register(Sprint)
admin.site.register(EstadoEmocional)
admin.site.register(Estado)
