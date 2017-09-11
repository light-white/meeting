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
    return render(request, 'news/news.html', {'contacts': contacts})

def article(request, nid):
    news = Article.objects.filter(id = nid).first()
    return render(request, 'news/article.html', {'news':news})
