from django.conf.urls import url
from django.shortcuts import render

from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^tasks/', tasks, name='tasks'),
    url(r'^self-tasks/', self_tasks, name='self-tasks'),
]
