# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from braces.views import LoginRequiredMixin
from .models import Proyecto, Sprint, HistoriaUsuario, Estado, Tarea, HistoriaUsuarioSprint

def kanban(request, nombre, sprintId):
    p = Proyecto.objects.get(nombre=nombre)
    s = Sprint.objects.filter(proyecto=p.pk)
    sprint = Sprint.objects.get(pk=sprintId);
    historiasUsuariosSprint = sprint.historiausuariosprint_set.all();
    hu = HistoriaUsuario.objects.filter(proyecto=p.pk)
    for h in hu:
        h.tareas = Tarea.objects.filter(historiaUs = h.pk)
    es = Estado.objects.all()
    return render(request, 'proyecto/proyecto_kanban.html', 
                 {
                     'proyecto':p, 
                     'sprints':s, 
                     'historiasU':hu,
                     'estados':es, 
                     'historiasUsuariosSprint' : historiasUsuariosSprint, 
                     'sprint' : sprint
                })
def tablero(request, nombre, sprintId):
    proyecto = Proyecto.objects.get(nombre=nombre)
    sprint = Sprint.objects.get(pk=sprintId)
    estados = Estado.objects.all()
    test = 'get';
    if request.method == 'POST':
        estado = request.POST.get('tarea_estado')
        tarea = request.POST.get('tarea_id')
        tarea = Tarea.objects.get(pk=tarea)
        tarea.estado = Estado.objects.get(pk=estado)
        tarea.save()
    
    return render(request, 'proyecto/tablero.html', {
         'proyecto' : proyecto,
         'sprint' : sprint,
         'estados' : estados,
         'test' : test
    })


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    slug_field = 'nombre'
    slug_url_kwarg = 'nombre'


class ProyectoKanbanView(LoginRequiredMixin, DetailView):
    template_name = 'proyecto/proyecto_kanban.html'
    model = Proyecto
    slug_field = 'nombre'
    slug_url_kwarg = 'nombre'


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto

