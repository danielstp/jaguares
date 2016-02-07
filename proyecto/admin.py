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
    extra = 1

class MiembroProyectoInline(admin.TabularInline):
    model = Miembro
    extra = 1

class DocumentoProyectoInline(NestedStackedInline):
    model = DocumentoProyecto
    extra = 1

class SprintInline(NestedStackedInline):
    model = Sprint
    extra = 1
    inlines = [DocumentoSprintInline]
    list_display = ('nombre','proyecto')
    list_filter = ['nombre','proyecto']


class ComentarioSprintInline(admin.TabularInline):
    model = ComentarioSprint
    extra = 1


class ComentarioProyectoInline(admin.TabularInline):
    model = ComentarioProyecto
    extra = 1


class ComentarioTareaInline(admin.TabularInline):
    model = ComentarioTarea
    extra = 1


class ProyectoAdmin(NestedStackedInline):
    model = Proyecto
    inlines = [SprintInline,]


class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    inlines = [MiembroProyectoInline, DocumentoProyectoInline, ComentarioProyectoInline, SprintInline,]


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
admin.site.register(HistoriaUsuario, HistoriaUsuarioAdmin)
admin.site.register(HistoriaTarea)
admin.site.register(Tarea)
admin.site.register(Rol)
admin.site.register(CriterioAceptacion)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(EstadoEmocional)
admin.site.register(Estado)
