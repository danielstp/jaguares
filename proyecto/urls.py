# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'proyecto'
urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.ProyectoListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^(?P<nombre>[\w.@+-]+)/$',
        view=views.ProyectoDetailView.as_view(),
        name='detail'
    ),

    url(
        regex=r'^(?P<nombre>[\w.@+-]+)/kanban/$',
        view=views.kanban,
        name='kanban'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.ProyectoUpdateView.as_view(),
        name='update'
    ),
]
