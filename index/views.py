from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from index.models import *
from news.models import *
from index.forms import *

# Create your views here.
def index(request):
    user = None
    news = list(Article.objects.all().order_by('time')[:6])
    images = list(Indeximage.objects.all())
    return render(request, 'index/index.html', {'images':images, 'news':news})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data
            user = authenticate(username=u['username'], password=u['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login')
            else:
                return HttpResponseRedirect('/login')
        else:
            return render(request, 'index/login.html', {'form':form})
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'index/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username'])
            if user:
                return render(request, 'index/register.html', {'form':form})
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.realname = form.cleaned_data['realname']
            user.university = form.cleaned_data['university']
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index/register.html', {'form':form})
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'index/register.html', {'form':form})

def user_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = PasswordForm()
            inform = InvoiceForm({'title':request.user.title, 'invoicenum':request.user.invoicenum, 'address':request.user.address, 'postal':request.user.postal, 'phone':request.user.phone})
            return render(request, 'index/user.html', {'form':form, 'inform':inform})
        else:
            return HttpResponseRedirect('/')

def change_password(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PasswordForm(request.POST)
            if form.is_valid():
                pwd = form.cleaned_data
                user = authenticate(username=request.user.username, password=pwd['password'])
                if user is not None and pwd['repwd'] == pwd['newpwd']:
                    user.set_password(pwd['repwd'])
                    user.save()
                else:
                    return render(request, 'index/user.html', {'form':form})
            return HttpResponseRedirect('/user')
        else:
            return HttpResponseRedirect('/')

def change_invoice(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = InvoiceForm(request.POST)
            if form.is_valid():
                invoice = form.cleaned_data
                user = request.user
                user.title = invoice['title']
                user.invoicenum = invoice['invoicenum']
                user.address = invoice['address']
                user.postal = invoice['postal']
                user.phone = invoice['phone']
                user.save()
            return HttpResponseRedirect('/user')
        else:
            return HttpResponseRedirect('/')

def about(request):
    return render(request, 'index/about.html')
