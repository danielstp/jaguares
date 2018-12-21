from __future__ import unicode_literals
from django.db                  import models
from django.conf                import settings
from django.utils.translation   import ugettext_lazy as _
from django.core.validators     import RegexValidator
from datetime                   import datetime
from polymorphic.models         import PolymorphicModel

class Comentario(PolymorphicModel):
    
    def resumen(self):
        return self.comentario[:120]
    
    comentario = models.TextField()
    fecha = models.DateTimeField(_(u'Fecha del comentario'),
                                default=datetime.now(), 
                                editable=False)

    def __str__(self):
        return self.resumen()


class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripción = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural= _(u'Roles')


class EstadoEmocional(models.Model):
    nombre = models.CharField(_(u'Estado Emocional'), max_length=30, default='')
    descripción = models.CharField(_(u'descripción'), max_length=250, default='')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Estados Emocionales')


class Estado(models.Model):
    nombre = models.CharField(_(u'Estado'), max_length=30, default='')
    descripción = models.CharField(_(u'descripción'), max_length=250, default='')

    def __str__(self):
        return self.nombre


class Prioridad(models.Model):
    nombre = models.CharField(_(u'Estado'), max_length=30, default='')
    descripción = models.CharField(_(u'descripción'), max_length=250, default='')
    valor = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = _(u'Prioridades')


class Proyecto(models.Model):
    nombre = models.CharField(_(u'Proyecto'), max_length=250, unique=True)
    descripción = models.CharField(_(u'Descripción'), max_length=250)
    creado = models.DateTimeField(default=datetime.now(), editable=False)
    fechaInicio = models.DateTimeField(_(u'Fecha inicio'), default=datetime.now(), editable=True)
    duración = models.DurationField(_(u'Duración (Dias hh:mm:ss)'))

    def __str__(self):
        return self.nombre


class ComentarioProyecto(Comentario):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)


class Miembro(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    persona = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)

    def __str__(self):
        return self.persona.get_username() + " (" + self.rol.nombre + ") Proy:" + self.proyecto.nombre


class Documento(PolymorphicModel):
    nombre =      models.CharField(_(u'Nombre'), max_length=250)
    descripción = models.CharField(_(u'Descripción'), max_length=250)
    creado =      models.DateTimeField(auto_now=True, editable=False)
    archivo =     models.FileField(upload_to=u'Documentos')
    dueño =       models.ForeignKey(Miembro, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Sprint(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    descripción = models.TextField(_(u'descripción'), default='')
    inicio = models.DateTimeField(default=datetime.now())
    fin = models.DateTimeField(default=datetime.now())
    finalizado = models.BooleanField(default=False)

    def _get_duración(self):
        return (self.fin - self.inicio).days

    duración = property(_get_duración)
    adjunto = models.ForeignKey(Documento, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return ('Sprint '+ self.nombre) 


class ComentarioSprint(Comentario):
    sprint = models.ForeignKey(Sprint, on_delete=models.PROTECT)
    def __str__(self):
        return self.sprint.nombre


class DocumentoSprint(Documento):
    sprintRef = models.ForeignKey(Sprint, on_delete=models.PROTECT)


class DocumentoProyecto(Documento):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = _(u'Documentos adjuntos Proyecto')


class HistoriaUsuario(models.Model):
    numeroHistoria = models.IntegerField(_(u'Nro. Historia'), default=0, editable=False)
    fechaElaboracion = models.DateTimeField(_(u'Fecha elaboración'), default=datetime.now(),editable=False)
    personaElaboro = models.CharField(_(u'Elaborado por'), max_length=200,default='', editable=False)
    titulo = models.TextField(_(u'Titulo'), default='')
    descripción = models.TextField(_(u'descripción'), default='')
    prioridad = models.ForeignKey(Prioridad, null=True, blank=True, on_delete=models.PROTECT)
    tiempoEstimado = models.DecimalField(_(u'Tiempo estimado'), default=0,max_digits=10,decimal_places=2)
    persona = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Responsable', null=True, blank=True, on_delete=models.PROTECT)
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
    
    def estaTerminado(self):
        tareas = self.tarea_set.all() 
        if len(tareas) == 0:
            return False
        for tarea in tareas:
            if tarea.estado.nombre != 'Done':
                return False
        return True
        
    class Meta:
        verbose_name_plural = _(u'Product Backlog')


class DocumentoHistoriaUsuario(Documento):
    historiaUsuario = models.ForeignKey(HistoriaUsuario, on_delete=models.PROTECT)


class CriterioAceptacion(models.Model):
    resumen = models.CharField(max_length=30)
    descripción = models.CharField(max_length=250)
    autor = models.ForeignKey(Miembro, on_delete=models.PROTECT)
    historiaUsuario = models.ForeignKey(HistoriaUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.resumen

    class Meta:
          verbose_name_plural = _(u'Criterios de aceptación')


class HistoriaUsuarioSprint(models.Model):
    historiaUsuario = models.ForeignKey(HistoriaUsuario, on_delete=models.PROTECT)
    sprint = models.ForeignKey(Sprint, limit_choices_to={'finalizado': False}, on_delete=models.PROTECT)

    def __str__(self):
        return self.sprint.nombre + " - " + self.historiaUsuario.titulo

    class Meta:
        verbose_name_plural = _(u'Asignacion HU - Sprint')


class Tarea(models.Model):
    titulo = models.CharField(_(u'Nombre'),max_length=200,default='')
    descripción = models.TextField(_(u'descripción'),default='')
    progreso = models.DecimalField('Progreso (de 0 a 100)',default=0,max_digits=10,decimal_places=2)
    documento = models.ForeignKey(Documento,null=True,blank=True, on_delete=models.PROTECT)
    miembro = models.ForeignKey(Miembro,null=True,blank=True, verbose_name='Responsable', on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado,default=1, on_delete=models.PROTECT)
    historiaUs = models.ForeignKey(HistoriaUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class ComentarioTarea(Comentario):
    tarea = models.ForeignKey(Tarea, on_delete=models.PROTECT)


class HistoriaTarea(models.Model):
    progreso = models.DecimalField(('Progreso'),max_digits=10,decimal_places=2)
    fecha = models.DateTimeField(('Fecha'),default=datetime.now(),editable=False)
    comentarios = models.TextField(default='')
    tarea = models.ForeignKey(Tarea, on_delete=models.PROTECT)

    def __str__(self):
        return self.tarea.titulo + self.progreso

    class Meta:
        verbose_name_plural = _(u'Historia de las Tareas')

