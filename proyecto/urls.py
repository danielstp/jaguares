# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.index,
        name='list'
    ),

    url(
        regex=r'^(?P<proyecto>[\w.@+-]+)/$',
        view=views.index,
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.index,
        name='update'
    ),
]
