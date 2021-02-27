from django.shortcuts import render

response = {}
# Create your views here.


def login(request):
    return render(request, 'login_page.html', response)


def tasks(request):
    return render(request, 'tasks.html', response)


def self_tasks(request):
    return render(request, 'self_tasks.html', response)