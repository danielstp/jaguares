# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from braces.views import LoginRequiredMixin
from .models import Proyecto, Sprint, HistoriaUsuario, Estado, Tarea, HistoriaUsuarioSprint, Miembro

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
        if request.POST.get('action') == 'tarea_crear':
           hu_id = request.POST.get('hu_id')
           tarea_nombre = request.POST.get('tarea_nombre')
           tarea_descripcion = request.POST.get('tarea_descripcion')
           historia = HistoriaUsuario.objects.get(pk=hu_id)
           tarea = Tarea.objects.create(titulo=tarea_nombre, descripción=tarea_descripcion, historiaUs=historia)
           tarea.save()
        else:  
            tarea = request.POST.get('tarea_id')
            titulo = request.POST.get('tarea_nombre')
            descripcion = request.POST.get('tarea_descripcion')
            responsable = request.POST.get('tarea_miembro')
            estado = request.POST.get('tarea_estado')
            if responsable == "0":
                responsable = None
            else:             
                responsable = Miembro.objects.get(pk=responsable)
            tarea = Tarea.objects.get(pk=tarea)
            tarea.estado = Estado.objects.get(pk=estado)
            tarea.miembro = responsable
            tarea.titulo = titulo
            tarea.descripción = descripcion
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

