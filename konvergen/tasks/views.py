from django.shortcuts import render, redirect
from .models import *
from .forms import *

response = {}
# Create your views here.


def signup(request):
    return render(request, 'signup.html', response)


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.create(username=username, password=password)
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
        return render(request, 'self_tasks.html', response)
    else:
        return redirect("/login")


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Tasks(name='file', file=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('/tasks')
    else:
        form = DocumentForm()  # A empty, unbound form
        return redirect('/tasks')


def assign_task(request, id):
    username = request.session["username"]
    file = Tasks.objects.filter(id=id).first()
    file.booked_by = username
    file.save()
    return redirect('/tasks')


def delete_task(request, id):
    username = request.session["username"]
    file = Tasks.objects.filter(id=id).first()
    file.status = 0
    file.save()
    return redirect('/tasks')


def logout(request):
    request.session.flush()
    return redirect("/login")
