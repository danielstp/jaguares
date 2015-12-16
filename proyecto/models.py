from django.db                  import models
from django.utils.translation   import ugettext_lazy as _
from django.core.validators     import RegexValidator
from django.contrib.auth.models import User
from datetime                   import datetime


class Persona(models.Model):
    def personaDefault(request):
        return request.user
    # This field is required.
    user = models.OneToOneField(User, default=personaDefault)

    def __unicode__(self):
        return self.name

class HistoriaTarea(models.Model):
    def __unicode__(self):
        return self.nombre


class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural= _(u'Roles')

class EstadoEmocional(models.Model):
    nombre = models.CharField(_(u'Estado'), max_length=30, default='')
    descripcion = models.CharField(_(u'Descripcion'), max_length=250, default='')
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = _(u'Estados Emocionales')

class Estado(models.Model):
    def __unicode__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(_(u'Proyecto'), max_length=250)
    descripcion = models.CharField(_(u'Descripción'), max_length=250)
    creado = models.DateTimeField(default=datetime.now(), editable=False)
    fechaInicio = models.DateTimeField(_(u'Fecha inicio'), default=datetime.now(), editable=True)
    def __unicode__(self):
        return self.nombre


class Miembro(models.Model):
    rol = models.ForeignKey(Rol)
    persona = models.ForeignKey(Persona)
    proyecto = models.ForeignKey(Proyecto)

    def __unicode__(self):
        return self.nombre


class Documento(models.Model):
    nombre =      models.CharField(_(u'Nombre'), max_length=250)
    descripcion = models.CharField(_(u'Descripción'), max_length=250)
    creado =      models.DateTimeField(auto_now=True, editable=False)
    archivo =     models.FileField(upload_to=u'Documentos')
    dueno =       models.ForeignKey(Miembro)

    def __unicode__(self):
        return self.nombre


class Sprint(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    descripcion = models.TextField(_(u'Descripcion'), default='')
    inicio = models.DateTimeField(default=datetime.now())
    fin = models.DateTimeField(default=datetime.now())
    duracion = models.DurationField()
    comentarios = models.CharField(max_length=250) 
    adjunto = models.ForeignKey(Documento)

    def __unicode__(self):
        return self.nombre


class Tarea(models.Model):
    titulo = models.CharField(_(u'Titulo'),max_length=200,default='')
    descripcion = models.TextField(_(u'Descripcion'),default='')
    tiempoInicioEstimado = models.DateTimeField(_(u'Fecha de Inicio (Estimado)'), default=datetime.now(), editable=True)
    tiempoFinalizacionEstimado = models.DateTimeField(_(u'Fecha de finalizacion (Estimado)'), default=datetime.now(), editable=True)
    documento = models.ForeignKey(Documento)
    miembro = models.ForeignKey(Miembro)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.nombre


class CriterioAceptacion(models.Model):
    resumen = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    miembro = models.ForeignKey(Miembro)
    tarea = models.ForeignKey(Tarea)

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = _(u'Criterios de Aceptacion')

class HistoriaUsuario(models.Model):
    numeroHistoria = models.IntegerField(_(u'Nro. Historia'), default=0)
    fechaElaboracion = models.DateTimeField(_(u'Fecha elaboracion'), default=datetime.now(),editable=False)
    personaElaboro = models.CharField(_(u'Elaborado por'), max_length=200,default='')
    titulo = models.TextField(_(u'Titulo'), default='')
    descripcion = models.TextField(_(u'Descripcion'), default='')
    prioridad = models.IntegerField(_(u'Prioridad'), default=0)
    tiempoEstimado = models.DecimalField(_(u'Tiempo estimado'), default=0,max_digits=10,decimal_places=0)
    persona = models.ForeignKey(Persona)
    tareas = models.ForeignKey(Tarea)
    documentos = models.ForeignKey(Documento)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _(u'Historias de Usuario')
    
