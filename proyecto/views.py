from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Proyecto

def index(request):
    p = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto.html', {'proyectos':p})
