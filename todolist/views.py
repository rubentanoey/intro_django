from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url = '/todolist/login/')
def show_todolist(request):
    todolist_objects = Task.objects.filter(user=request.user)
    context = {"todolist": todolist_objects, "username": request.user}
    return render(request, "todolist.html", context)

@login_required(login_url = '/todolist/login/')
def add_task(request):
    user_name = User.objects.get(username=request.user)    
    form = TodolistForm()
    new_task = None
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'add_task.html', context)

@login_required(login_url = "/todolist/login/")
def mark_finished_task(request, id):
    task = Task.objects.get(user = request.user, id=id)
    task.is_finished = not (task.is_finished)
    task.save(update_fields = ["is_finished"])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))
    
@login_required(login_url = "/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id = id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))