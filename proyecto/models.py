from django.db                import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators   import RegexValidator


class Proyecto(models.Model):
    nombre = models.CharField(_(u'Proyecto'), max_length=250)

    def __unicode__(self):
        return self.nombre

class Miembro(models.Model):
    nombre = models.CharField(_(u'Miembro'), max_length=250)

    def __unicode__(self):
        return self.nombre

class Documento(models.Model):
   nombre=models.CharField(_(u'nombre'), max_length=250)
   descripcion=models.CharField(_(u'descripcion'), max_length=250)
   fecha=models.DateTimeField(auto_now=True, editable=False)
   archivo=models.FileField(upload_to=u'documentos')
   dueno=models.ForeignKey(Miembro)
   def __unicode__(self):
     return self.nombre

