from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from meet.models import *
from meet.forms import *
from index.models import User
from urllib import parse
from openpyxl import Workbook
from io import BytesIO
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
        meet = Meet.objects.filter(id = mid).first()
        form = JoinForm(request.POST)
        if form.is_valid():
            member = Meetmember()
            member.mid = mid
            member.uid = request.user.id
            if int(form.cleaned_data['pnum']) < 1:
                script = r'alert("人数不能少于1")'
                return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form, 'script':script})
            member.pnum = form.cleaned_data['pnum']
            member.livable = form.cleaned_data['livable']
            if member.livable != '不住宿':
                if form.cleaned_data['indate'] and form.cleaned_data['outdate']:
                    member.indate = form.cleaned_data['indate']
                    member.outdate = form.cleaned_data['outdate']
                else:
                    script = r'alert("住宿需填写住宿时间")'
                    return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form, 'script':script})
            member.invoice = form.cleaned_data['invoice']
            member.save()
            return HttpResponseRedirect('/meet/%s' % mid)
        else:
            meet = Meet.objects.filter(id = mid).first()
            return render(request, 'meet/meetjoin.html', {'meet':meet, 'form':form})

def memberitem(request, mid):
    if request.user.is_active:
        user = User.objects.get(id = request.user.id)
        meet = Meet.objects.filter(id = mid).first()
        meetmember = Meetmember.objects.filter(mid = mid).first()
        return render(request, 'meet/memberitem.html', {'meet':meet, 'member':meetmember})
    else:
        return HttpResponseRedirect(reverse('index-login'))

def memberexcel(request, mid):
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
        wb = Workbook()
        ws = wb.active
        ws.append(['学校名称', '报名人', '参会人数', '住宿', '入住时间', '离开时间', '发票'])
        for user in member:
            univer = user.university
            realname = user.realname
            pnum = user.pnum
            livable = user.livable
            if user.indate:
                indate = user.indate
            else:
                indate = ''
            if user.outdate:
                outdate = user.outdate
            else:
                outdate = ''
            if user.invoice:
                invoice = 'Y'
            else:
                invoice = ''
            ws.append([univer, realname, pnum, livable, indate, outdate, invoice])
        ws.column_dimensions['A'].width = 20
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 15
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 15
        ws.column_dimensions['G'].width = 15
        output = BytesIO()
        wb.save(output)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        filename = meet.title + '_member'
        filename = parse.quote(filename)
        response['Content-Disposition'] = 'attachment;filename={}.xlsx'.format(filename)
        response.write(output.getvalue())
        return response
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
            member.append(user)
        member.sort(key = lambda obj:obj.university)
        return render(request, 'meet/invoicemember.html', {'meet':meet, 'member':member})
    else:
        return HttpResponseRedirect(reverse('index-login'))

def invoiceexcel(request, mid):
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        meet = Meet.objects.filter(id = mid).first()
        meetmember = Meetmember.objects.filter(mid = mid, invoice=True)
        member = []
        for m in meetmember:
            user = User.objects.get(id = m.uid)
            member.append(user)
        member.sort(key = lambda obj:obj.university)
        wb = Workbook()
        ws = wb.active
        ws.append(['报名人', '发票抬头', '纳税人识别号', '快递地址', '邮政编码', '手机号'])
        for user in member:
            realname = user.realname
            title = user.title
            invoicenum = user.invoicenum
            address = user.address
            postal = user.postal
            phone = user.phone
            ws.append([realname, title, invoicenum, address, postal, phone])
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 15
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 15
        output = BytesIO()
        wb.save(output)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        filename = meet.title + '_invoice'
        filename = parse.quote(filename)
        response['Content-Disposition'] = 'attachment;filename={}.xlsx'.format(filename)
        response.write(output.getvalue())
        return response
    else:
        return HttpResponseRedirect(reverse('index-login'))
