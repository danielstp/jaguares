from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from django.utils.safestring import mark_safe

from .models import Documento
from .models import DocumentoSprint
from .models import DocumentoHistoriaUsuario
from .models import DocumentoProyecto
from .models import ComentarioTarea
from .models import ComentarioProyecto
from .models import ComentarioSprint
from .models import Proyecto
from .models import Miembro
from .models import HistoriaUsuario
from .models import HistoriaUsuarioSprint
from .models import HistoriaTarea
from .models import Tarea
from .models import Rol
from .models import CriterioAceptacion
from .models import Sprint
from .models import EstadoEmocional
from .models import Estado
from .models import Prioridad


class HistoriaUsuarioSprintInline(NestedStackedInline):
    model = HistoriaUsuarioSprint
    extra = 1
    verbose_name = "Sprint - HU :"


class DocumentoSprintInline(NestedStackedInline):
    model = DocumentoSprint
    extra = 1


class DocumentoHistoriaUsuarioInline(NestedStackedInline):
    model = DocumentoHistoriaUsuario
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

class TareaHistoriaUsuarioInline(admin.TabularInline):
    model = Tarea
    extra = 1


class ProyectoAdmin(NestedStackedInline):
    model = Proyecto
    inlines = [SprintInline,]


class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    inlines = [MiembroProyectoInline, DocumentoProyectoInline, ComentarioProyectoInline, SprintInline,]


class CriterioAceptacionInline(admin.TabularInline):
    model = CriterioAceptacion
    extra = 1

class SprintAdmin(admin.ModelAdmin):
    list_display = ('nombre','proyecto')
    list_filter = ['nombre','proyecto']
    inlines = [HistoriaUsuarioSprintInline,ComentarioSprintInline,]


class HistoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('titulo','fechaElaboracion','personaElaboro','persona','proyecto')
    list_filter = ['fechaElaboracion','personaElaboro','titulo','prioridad','persona','proyecto',]
    inlines = [HistoriaUsuarioSprintInline,CriterioAceptacionInline,DocumentoHistoriaUsuarioInline]


class CriterioAceptacionAdmin(admin.ModelAdmin):
    list_display = ('resumen','autor','historiaUsuario')
    list_filter = ['autor', 'historiaUsuario']

class TareaHistoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'progreso', 'documento')
    list_filter = ['autor', 'historiaUsuario']


admin.site.register(Documento)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Miembro)
admin.site.register(HistoriaUsuario, HistoriaUsuarioAdmin)
admin.site.register(HistoriaTarea)
admin.site.register(Tarea)
admin.site.register(Rol)
admin.site.register(CriterioAceptacion, CriterioAceptacionAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(EstadoEmocional)
admin.site.register(Estado)
admin.site.register(Prioridad)
