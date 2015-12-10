from django.contrib import admin
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from proyecto.models import Documento
from proyecto.models import DocumentoSprint
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

class DocumentoSprintInline(NestedStackedInline):
    model = DocumentoSprint

class SprintInline(NestedStackedInline):
    model = Sprint
    inlines = [DocumentoSprintInline]


class ProyectoAdmin(NestedStackedInline):
    model = Proyecto
    inlines = [SprintInline]


admin.site.register(Documento)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Miembro)
admin.site.register(Persona)
admin.site.register(HistoriaUsuario)
admin.site.register(HistoriaTarea)
admin.site.register(Tarea)
admin.site.register(Rol)
admin.site.register(CriterioAceptacion)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(EstadoEmocional)
admin.site.register(Estado)
