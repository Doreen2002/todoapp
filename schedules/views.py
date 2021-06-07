from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import *
def register(request):
   
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"acccount was created" + user)
            return redirect('login')
    context ={'form':form}
    return render(request, 'schedules/register.html', context)

def loginuser(request):
    context = {}
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'username incoorect is incorrect')
    return render(request, 'schedules/login.html', context)
def logoutuser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def index(request):
    form = ScheduledForm()
    scheduled = schedules.objects.all()
  
    if request.method =="POST":
        form = ScheduledForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    context = {
        'scheduled':scheduled,
        'form':form
       
    }
    return render(request,'schedules/index.html', context)
def updates(request, pkey):
    schedule = schedules.objects.get(id=pkey)
    form = ScheduledForm(instance=schedule)
    if request.method =='POST':
        form = ScheduledForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
        return redirect('')
    context={'form':form}
    return render(request, 'schedules/update.html', context)
def delete (request,pkey):
    
    item = schedules.objects.get(id=pkey)
    if request.method =='POST':
        item.delete()  
        return redirect('')
    context = {
     'item':item,
    }
    return render(request, 'schedules/delete.html', context)