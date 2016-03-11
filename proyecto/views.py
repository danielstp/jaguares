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

