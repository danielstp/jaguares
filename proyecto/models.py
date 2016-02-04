from __future__ import unicode_literals
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _
from django.core.validators     import RegexValidator
from django.contrib.auth.models import User
from datetime                   import datetime
from polymorphic.models         import PolymorphicModel

class Comentario(PolymorphicModel):
    resumen = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha = models.DateTimeField(_(u'Fecha inicio'), default=datetime.now(), editable=False)

    def __str__(self):
        return self.resumen


class Persona(models.Model):
    @classmethod
    def getUser(cls, request):
        user = getattr(request, "user", None)
        return Persona._default_manager.get(user=user)

    # This field is required.
    user = models.OneToOneField(User, related_name="cuenta", verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()


class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripción = models.CharField(max_length=250)

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


class Proyecto(models.Model):
    nombre = models.CharField(_(u'Proyecto'), max_length=250)
    descripción = models.CharField(_(u'Descripción'), max_length=250)
    creado = models.DateTimeField(default=datetime.now(), editable=False)
    fechaInicio = models.DateTimeField(_(u'Fecha inicio'), default=datetime.now(), editable=True)
    duración = models.DurationField(_(u'Duración (Dias hh:mm:ss)'))

    def __str__(self):
        return self.nombre


class ComentarioProyecto(Comentario):
    proyecto = models.ForeignKey(Proyecto)


class Miembro(models.Model):
    rol = models.ForeignKey(Rol)
    persona = models.ForeignKey(Persona)
    proyecto = models.ForeignKey(Proyecto)

    def __str__(self):
        return self.nombre


class Documento(PolymorphicModel):
    nombre =      models.CharField(_(u'Nombre'), max_length=250)
    descripción = models.CharField(_(u'Descripción'), max_length=250)
    creado =      models.DateTimeField(auto_now=True, editable=False)
    archivo =     models.FileField(upload_to=u'Documentos')
    dueño =       models.ForeignKey(Miembro)

    def __str__(self):
        return self.nombre


class Sprint(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=250)
    proyecto = models.ForeignKey(Proyecto)
    descripción = models.TextField(_(u'descripción'), default='')
    inicio = models.DateTimeField(default=datetime.now())
    fin = models.DateTimeField(default=datetime.now())
    
    def _get_duración(self):
        return (self.fin - self.inicio).days
    
    duración = property(_get_duración)
    adjunto = models.ForeignKey(Documento, null=True, blank=True)
    
    def __str__(self):
        return ((self.descripción + ' (%d dias)') % self.duración)


class ComentarioSprint(Comentario):
    sprint = models.ForeignKey(Sprint)
    def __str__(self):
        return self.sprint.nombre


class DocumentoSprint(Documento):
    sprintRef = models.ForeignKey(Sprint)


class DocumentoProyecto(Documento):
    proyecto = models.ForeignKey(Proyecto)

    class Meta:
        verbose_name_plural = _(u'Documentos adjuntos Proyecto')


class HistoriaUsuario(models.Model):
    numeroHistoria = models.IntegerField(_(u'Nro. Historia'), default=0)
    fechaElaboracion = models.DateTimeField(_(u'Fecha elaboración'), default=datetime.now(),editable=False)
    personaElaboro = models.CharField(_(u'Elaborado por'), max_length=200,default='')
    titulo = models.TextField(_(u'Titulo'), default='')
    descripción = models.TextField(_(u'descripción'), default='')
    prioridad = models.IntegerField(_(u'Prioridad'), default=0)
    tiempoEstimado = models.DecimalField(_(u'Tiempo estimado'), default=0,max_digits=10,decimal_places=2)
    persona = models.ForeignKey(Persona)
    documentos = models.ForeignKey(Documento)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = _(u'Historias de Usuario')


class Tarea(models.Model):
    titulo = models.CharField(_(u'Titulo'),max_length=200,default='')
    descripción = models.TextField(_(u'descripción'),default='')
    tiempoInicioEstimado = models.DateTimeField(_(u'Fecha de Inicio (Estimado)'), default=datetime.now())
    tiempoFinalizacionEstimado = models.DateTimeField(_(u'Fecha de finalizacion (Estimado)'), default=datetime.now())
    progreso = models.DecimalField('Progreso (de 0 a 100))',default=0,max_digits=10,decimal_places=2)
    documento = models.ForeignKey(Documento)
    miembro = models.ForeignKey(Miembro)
    estado = models.ForeignKey(Estado)
    historiaUs = models.ForeignKey(HistoriaUsuario)

    def __str__(self):
        return self.titulo


class ComentarioTarea(Comentario):
    tarea = models.ForeignKey(Tarea)


class HistoriaTarea(models.Model):
    progreso = models.DecimalField(('Progreso'),max_digits=10,decimal_places=2)
    fecha = models.DateTimeField(('Fecha'),default=datetime.now(),editable=False)
    comentarios = models.TextField(default='')
    tarea = models.ForeignKey(Tarea)
    def __str__(self):
        return self.tarea.titulo + self.progreso


class CriterioAceptacion(models.Model):
    resumen = models.CharField(max_length=30)
    descripción = models.CharField(max_length=250)
    miembro = models.ForeignKey(Miembro)
    tarea = models.ForeignKey(Tarea)

    def __str__(self):
        return self.resumen

    class Meta:
          verbose_name_plural = _(u'Criterios de aceptación')
