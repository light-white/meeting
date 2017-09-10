from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from history.models import *

# Create your views here.

def history(request):
    historylist = History.objects.all()
    paginator = Paginator(historylist, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'history/history.html', {'contacts': contacts})

def historyitem(request, hid):
    history = History.objects.filter(id = hid).first()
    return render(request, 'history/historyitem.html', {'history':history})
