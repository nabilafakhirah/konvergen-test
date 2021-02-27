from django.shortcuts import render, redirect

from konvergen import settings
from .models import *
from .forms import *

import os
from django.http import HttpResponse, Http404

response = {}
# Create your views here.


def signup(request):
    response['message'] = 'yes'
    return render(request, 'signup.html', response)


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.create(username=username, password=password)
        response['message'] = 'yes'
        return redirect("/login")


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = UserProfile.objects.filter(username=username, password=password)
        if user.exists():
            request.session['username'] = username
            return redirect("/tasks")
        else:
            response['message'] = "no"
            return redirect("/login")


def login(request):
    return render(request, 'login_page.html', response)


def tasks(request):
    if request.session.has_key('username'):
        files = Tasks.objects.filter(status=1)
        response['files'] = files
        return render(request, 'tasks.html', response)
    else:
        return redirect("/login")


def self_tasks(request):
    if request.session.has_key('username'):
        username = request.session["username"]
        files = Tasks.objects.filter(status=1, booked_by=username)
        response['files'] = files
        response['username'] = username
        return render(request, 'self_tasks.html', response)
    else:
        return redirect("/login")


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Tasks(name='file', file=request.FILES['docfile'])
            newdoc.save()

            return redirect('/tasks')
    else:
        return redirect('/tasks')


def assign_task(request, id):
    username = request.session["username"]
    file = Tasks.objects.filter(id=id).first()
    file.booked_by = username
    file.save()
    return redirect('/tasks')


def revoke_task(request, id):
    file = Tasks.objects.filter(id=id).first()
    file.booked_by = ""
    file.save()
    return redirect('/self-tasks')


def delete_task(request, id):
    username = request.session["username"]
    file = Tasks.objects.filter(id=id).first()
    file.status = 0
    file.save()
    return redirect('/tasks')


def download(request, id):
    obj = Tasks.objects.get(id=id)
    path = obj.file.path
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            res = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            res['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return res
    raise Http404


def logout(request):
    request.session.flush()
    return redirect("/login")
