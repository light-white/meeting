from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from meet.models import *
from meet.forms import *
from index.models import User
# Create your views here.

def meet(request):
    meetlist = Meet.objects.all()
    paginator = Paginator(meetlist, 10) # Show 25 contacts per page
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
        pagelist = list(range(contacts.paginator.num_pages-9,contacts.paginator.num_pages+1))
    else:
        pagelist = list(range(contacts.number-4,contacts.number+6))
    return render(request, 'meet/meet.html', {'contacts': contacts, 'pagelist':pagelist})

def meetitem(request, mid):
    meet = Meet.objects.filter(id = mid).first()
    status = 0
    if Meetmember.objects.filter(mid = mid, uid = request.user.id):
        status = 1
    return render(request, 'meet/meetitem.html', {'meet':meet, 'status':status})

def joinmeet(request, mid):
    if request.method == 'GET':
        if request.user.is_active:
            meet = Meet.objects.filter(id = mid).first()
            form = JoinForm()
            return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form})
        else:
            return HttpResponseRedirect(reverse('index-login'))
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            member = Meetmember()
            member.mid = mid
            member.uid = request.user.id
            member.pnum = form.cleaned_data['pnum']
            member.livable = form.cleaned_data['livable']
            if member.livable != '不住宿':
                if form.cleaned_data['indate'] and form.cleaned_data['outdate']:
                    member.indate = form.cleaned_data['indate']
                    member.outdate = form.cleaned_data['outdate']
                else:
                    meet = Meet.objects.filter(id = mid).first()
                    return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form})
            member.invoice = form.cleaned_data['invoice']
            member.save()
            return HttpResponseRedirect('/meet/%s' % mid)
        else:
            meet = Meet.objects.filter(id = mid).first()
            return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form})

def memberitem(request, mid):
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        meet = Meet.objects.filter(id = mid).first()
        meetmember = Meetmember.objects.filter(mid = mid).first()
        return render(request, 'meet/memberitem.html', {'meet':meet, 'member':meetmember})
    else:
        return HttpResponseRedirect(reverse('index-login'))

def meetmember(request, mid):
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        meet = Meet.objects.filter(id = mid).first()
        meetmember = Meetmember.objects.filter(mid = mid)
        member = []
        for m in meetmember:
            user = User.objects.get(id = m.uid)
            user.pnum = m.pnum
            user.livable = m.livable
            user.indate = m.indate
            user.outdate = m.outdate
            user.invoice = m.invoice
            member.append(user)
        member.sort(key = lambda obj:obj.university)
        return render(request, 'meet/meetmember.html', {'meet':meet, 'member':member})
    else:
        return HttpResponseRedirect(reverse('index-login'))

def invoicemember(request, mid):
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        meet = Meet.objects.filter(id = mid).first()
        meetmember = Meetmember.objects.filter(mid = mid, invoice=True)
        member = []
        for m in meetmember:
            user = User.objects.get(id = m.uid)
            print(user.title)
            member.append(user)
        member.sort(key = lambda obj:obj.university)
        return render(request, 'meet/invoicemember.html', {'meet':meet, 'member':member})
    else:
        return HttpResponseRedirect(reverse('index-login'))
