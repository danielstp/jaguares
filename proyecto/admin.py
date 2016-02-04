from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from proyecto.models import Documento
from proyecto.models import DocumentoSprint
from proyecto.models import DocumentoProyecto
from proyecto.models import ComentarioTarea
from proyecto.models import ComentarioProyecto
from proyecto.models import ComentarioSprint
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

class DocumentoProyectoInline(NestedStackedInline):
    model = DocumentoProyecto

class SprintInline(NestedStackedInline):
    model = Sprint
    inlines = [DocumentoSprintInline]
    list_display = ('nombre','proyecto')
    list_filter = ['nombre','proyecto']


class ProyectoAdmin(NestedStackedInline):
    model = Proyecto
    inlines = [SprintInline]

class ComentarioSprintInline(admin.TabularInline):
    model = ComentarioSprint


class ComentarioProyectoInline(admin.TabularInline):
    model = ComentarioProyecto


class ComentarioTareaInline(admin.TabularInline):
    model = ComentarioTarea


class ProyectoAdmin(admin.ModelAdmin):
    inlines = [SprintInline, DocumentoProyectoInline, ComentarioProyectoInline]

class SprintAdmin(admin.ModelAdmin):
    list_display = ('nombre','proyecto')
    list_filter = ['nombre','proyecto']
    inlines = [ComentarioSprintInline,]


class HistoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('titulo','fechaElaboracion','personaElaboro','persona','proyecto')
    list_filter = ['fechaElaboracion','personaElaboro','titulo','prioridad','persona','proyecto','sprint']

admin.site.register(Documento)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Miembro)
admin.site.register(Persona)
admin.site.register(HistoriaUsuario, HistoriaUsuarioAdmin)
admin.site.register(HistoriaTarea)
admin.site.register(Tarea)
admin.site.register(Rol)
admin.site.register(CriterioAceptacion)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(EstadoEmocional)
admin.site.register(Estado)
