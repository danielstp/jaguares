from django.db                import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators   import RegexValidator
from datetime                 import datetime


class HistoriaUsuario(models.Model):
    def __unicode__(self):
        return self.nombre


class HistoriaTarea(models.Model):
    def __unicode__(self):
        return self.nombre


class Tarea(models.Model):
    def __unicode__(self):
        return self.nombre


class Rol(models.Model):
    def __unicode__(self):
        return self.nombre


class CriterioAceptacion(models.Model):
    def __unicode__(self):
        return self.nombre


class Sprint(models.Model):
    def __unicode__(self):
        return self.nombre


class EstadoEmocional(models.Model):
    def __unicode__(self):
        return self.nombre


class Estado(models.Model):
    def __unicode__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(_(u'Proyecto'), max_length=250)
    descripcion = models.CharField(_(u'Descripción'), max_length=250)
    creado = models.DateTimeField(default=datetime.now(), editable=False)

    def __unicode__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(_(u'Miembro'), max_length=250)

    def __unicode__(self):
        return self.nombre


class Miembro(models.Model):
    persona = models.ForeignKey(Persona,default=)
    proyecto = models.ForeignKey(Proyecto)
    def __unicode__(self):
        return self.nombre


class Documento(models.Model):
   nombre      = models.CharField(_(u'Nombre'), max_length=250)
   descripcion = models.CharField(_(u'Descripción'), max_length=250)
   creado      = models.DateTimeField(auto_now=True, editable=False)
   archivo     = models.FileField(upload_to=u'Documentos')
   dueno       = models.ForeignKey(Miembro)
   def __unicode__(self):
     return self.nombre

