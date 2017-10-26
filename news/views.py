from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import *

def news(request):
    newslist = Article.objects.all()
    paginator = Paginator(newslist, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    if contacts.paginator.num_pages < 10:
        pagelist = list(range(1,contacts.paginator.num_pages+1))
    elif contacts.number < 5:
        pagelist = list(range(1,11))
    elif contacts.paginator.num_pages-contacts.number < 5:
        pagelist = list(range(contacts.paginator.num_pages-10,contacts.paginator.num_pages+1))
    else:
        pagelist = list(range(contacts.number-4,contacts.number+6))
    return render(request, 'news/news.html', {'contacts': contacts, 'pagelist':pagelist})

def article(request, nid):
    news = Article.objects.filter(id = nid).first()
    return render(request, 'news/article.html', {'news':news})
