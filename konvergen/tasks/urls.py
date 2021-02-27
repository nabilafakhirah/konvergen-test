from django.conf.urls import url
from django.shortcuts import render

from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^tasks/', tasks, name='tasks'),
    url(r'^self-tasks/', self_tasks, name='self-tasks'),


    url(r'^sign-up/', sign_up, name='sign-up'),
    url(r'^log-in/', log_in, name='log-in'),
    url(r'^upload/', model_form_upload, name='upload'),

    url(r'^assign-task/(?P<id>\w+)', assign_task, name='assign-task'),
    url(r'^delete-task/(?P<id>\w+)', delete_task, name='delete-task'),
    url(r'^revoke-task/(?P<id>\w+)', revoke_task, name='revoke-task'),
    url(r'^download/(?P<id>\w+)', download, name='download'),
]
