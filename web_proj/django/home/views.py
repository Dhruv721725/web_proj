from django.shortcuts import render, redirect,HttpResponse
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
# Create your views here.
# CRUD
@login_required(login_url='/login/')
def home(req):
    data=Recipies.objects.all().order_by('name')
    if req.method=='GET':
        dat=req.GET.get('search')
        if dat==None:
            dat=''
        new_data=[]
        for i in data:
            if str(dat).lower() in str(i.name).lower():
                new_data.append(i)
        data=new_data
    
    context={'data':data}
    return render(req,'recipies.html',context)

def upload(req):
    if req.method =='POST':
        data=req.POST
        n=data.get('rname')
        d=data.get('rdesc')
        i=req.FILES.get('rimage')
        Recipies.objects.create(name=n,desc=d,img=i)
        return redirect('/home/')
    return render(req,'upload.html')

def del_rcp(req,id):
    Recipies.objects.get(id=id).delete()
    return redirect('/home/')

def upd_rcp(req,id):
    data=Recipies.objects.filter(id=id)
    if req.method=='POST':
        data=req.POST
        n=data.get('rname')
        d=data.get('rdesc')
        i=req.FILES.get('rimage')
        if n!=data.get('name') : 
            item=Recipies.objects.get(id=id)
            item.name=n
            item.save()
        if d!=data.get('desc'):
            item=Recipies.objects.get(id=id)
            item.desc=d
            item.save()
        if str(i).lower()!='none':
            item=Recipies.objects.get(id=id)
            item.img=i
            item.save()
        return redirect ('/home/')
    data=Recipies.objects.get(id=id)
    return render(req,'upd.html',context={'data':data})

# LOGIN /REGISTER
def login_page(req):

    if req.method=='POST':
        data=req.POST
        usrname=data.get('usrname')
        pswd=data.get('pass')
        
        user=User.objects.filter(username=usrname)
        if user.exists():
            check=authenticate(username=usrname,password=pswd)
            
            if check==None:
                messages.info(req,'invalid password')
                return redirect('/login/')
            else:
                # entry here
                login(req,check)
                return redirect('/home/')
            
        else:
            messages.info (req,"user not exists")
            return redirect('/login/')
    return render(req,'login.html')

def register(req):
    if req.method=='POST':
        data=req.POST
        nm=data.get('name')
        em=data.get('email')
        pswd=data.get('pass')
        usrname=data.get('usrname') 

        user=User.objects.filter(username=usrname)
        if user.exists():
            messages.info(req,'username already taken')
            return redirect('/register/')

        user = User.objects.create(username=usrname,first_name=nm,email=em)
        user.set_password(pswd)
        user.save()
        messages.info(req,'from now onwards you are the certified user of our website')
        return redirect('/register/')
    return render(req,'register.html')

def logout_page(req):
    logout(req)
    messages.info(req,'successfully loged out')
    return redirect('/login/')

def get_st(req):
    if req.method=='GET':
        qset=Student.objects.all()
        dat=req.GET.get('search')
        if dat!=None:
            qset=Student.objects.filter(Q(st_name__icontains=dat )|
                                        Q(department__department__icontains=dat)|
                                        Q(st_id__st_id__icontains=dat)|
                                        Q(st_age__icontains=dat)|
                                        Q(st_address__icontains=dat))

        page=Paginator(qset,10)
        page_no=req.GET.get('page')
        page_obj=page.get_page(page_no)
    return render(req,'student.html',context={'data':page_obj})

def see_marks(req,id):
    nm_obj=Student.objects.filter(id=id)
    name=nm_obj[0].st_name
    qset=Sub_marks.objects.filter(st_name__st_name=name)

    no_sub=Sub_marks.objects.filter(st_name__st_name=name).count()
    tot=Sub_marks.objects.filter(st_name__st_name=name).aggregate(Sum('marks'))['marks__sum']
    prcnt=tot*100/(no_sub*100)

    stid=Student.objects.get(id=id).st_id
    ranks=Student.objects.annotate(marks=Sum('st_marks__marks')).order_by('-marks','-st_age')
    rank=0
    for r in ranks:
        rank+=1
        if stid==r.st_id:
            break
    context={'data':qset,'name':name,'id':id,'course':nm_obj[0].department,'prcnt':prcnt,'rank':rank}
    return render(req,'marks.html',context)
# def next_pg(req,pg):
#     num=int(pg)
#     num+=1
#     qset=Student.objects.all()
#     page=Paginator(qset,30)
#     page_obj=page.get_page(num)
#     return render(req,'student.html',context={'data':page_obj,'pg':num})
