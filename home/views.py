from django.shortcuts import render,redirect
from .models import member,bill,car,consume,myshop,friend
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup
import requests
import datetime
import time,math
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import memberSerializer
class memberViewSet(viewsets.ModelViewSet):
    queryset=member.objects.all()
    serializer_class=memberSerializer
    permission_classes=(AllowAny,)

def toindex(request):
    return redirect('/home/index/')
def index(request):
    if not "login" in request.session:
            messages.error(request,"尚未登入喔,請先登入")
            return render(request,'home/innerpage/login.html',locals())
    elif "userac" in request.session:
            Ac=request.session['userac']
            r1=member.objects.get(memberAc=Ac)
            point=str(r1.memberPt)
            request.session['point']=point
            if 'check' in request.session:
                check=True
            else:
                check=False
            return render(request,'home/index.html',locals())
    else:
        return render(request,'home/index.html')
def simple_crawl(request):
     url = "https://www1.cycu.edu.tw/"
     res = requests.get(url)
     soup = BeautifulSoup(res.text,"html.parser")
     title = soup.select('title')
     return render(request,'home/home.html',locals())
def hello(request):
    name=request.GET['name']
    gender=request.GET['gender']
    c={'g':gender}
    c['who']=name
    return render(request,'home/hello.html',c)
def signup1(request):
    mName=request.GET['memberName']
    mAc=request.GET['memberAc']
    mPw=request.GET['memberPw']
    mTel=request.GET['memberphone']
    mEml=request.GET['memberEmail']
    mAdr=request.GET['memberAddress']
    a=member.objects.filter(memberAc=mAc)
    if a.exists():
        messages.error(request,'帳號已存在,請使用已有帳戶登入')
        return render(request,'home/innerpage/login.html',locals())
    else:
        messages.error(request,'註冊成功!恭喜您成為為環保付出的一份子')
        user=member.objects.create(memberAc=mAc,memberPw=mPw,memberName=mName,memberTel=mTel,memberEml=mEml,memberAdr=mAdr)
        user.save()
        return render(request,'home/innerpage/login.html',locals())
def login1(request):
    Ac=request.GET['memberAc']
    Pw=request.GET['memberPw']
    b=member.objects.filter(memberAc=Ac,memberPw=Pw)
    if b.exists():
        request.session['login']='y'
        request.session['userac']=Ac
        point=str(b[0].memberPt)
        request.session['point']=point
        messages.error(request,b[0].memberName+'登入成功!一起為環保努力吧')
        return render(request,'home/index.html',locals())
    else:
        messages.error(request,'帳號或密碼不符,請重新輸入')
        return render(request,'home/innerpage/login.html',locals())
def logout(request):
    del request.session['login']
    del request.session['userac']
    del request.session['point']
    del request.session['check']
    messages.error(request,'您已登出,感謝您對環保的付出')
    return render(request,'home/innerpage/login.html')
def signup(request):
    return render(request,'home/innerpage/signup.html')
def consume1(request):
    if request.method=="GET":
        Ac=request.session['userac']
        carname=request.GET['carName']
        carnum=request.GET['carNum']
        usetime=int(request.GET['usetime'])
        usepoint=int(request.GET['realusepoint'])
        name='跑車'
        pt=int(request.session['point'])
        updatept=pt-usepoint
        a=consume.objects.create(memberAc=Ac,carName=carname,carNum=carnum,usePt=usepoint,useSec=usetime,consumeName=name)
        a.save()
        request.session['point']=str(updatept)
        b=member.objects.filter(memberAc=Ac).update(memberPt=updatept)
        return redirect('/home/pointrecord/')
    else:
        return render(request,'home/innerpage/car1_used.html',locals())
def pointrecord(request):
        consumes=consume.objects.order_by("-id")   
        point=request.session['point']
        return render(request,'home/innerpage/pointrecord.html',locals())
def petwarehouse(request):
    return render(request,'home/innerpage/petwarehouse.html')
def perconsent(request):
    return render(request,'home/innerpage/per-consent.html')
def noticenter(request):
    return render(request,'home/innerpage/noticenter.html')
def mystore(request):
    mystores=myshop.objects.all()
    return render(request,'home/innerpage/mystore.html',locals())
def mypet(request):
    return render(request,'home/innerpage/mypet.html')
def myfriends(request):
    Ac=request.session['userac']
    friends=friend.objects.filter(memberAc=Ac)
    return render(request,'home/innerpage/myfriends.html',locals())
def mycoupon(request):
    return render(request,'home/innerpage/mycoupon.html')
def addcar(request):
    return render(request,'home/innerpage/addcar.html')
def addcar1(request):
    Ac=request.session['userac']
    carnum=request.GET['carnum']
    carimg="img/maserati1.jpg"
    if carnum=="AAA-8888":
        a=car.objects.create(memberAc=Ac,carName='MC20',carImg=carimg,carNum=carnum,carEv=1500)
        a.save()
        messages.error(request,'新增成功')
    else:
        messages.error(request,'此車牌找不到匹配的車輛')
    return redirect('/home/garage/')
def modifymem(request):
    Ac=request.session['userac']
    user=member.objects.filter(memberAc=Ac)
    memberName=user[0].memberName
    memTel=user[0].memberTel
    memAdr=user[0].memberAdr
    memEml=user[0].memberEml
    return render(request,'home/innerpage/modifymem.html',locals())
def login(request):
    return render(request,'home/innerpage/login.html')
def leaderboard(request):
    return render(request,'home/innerpage/leaderboard.html')
def helpcenter(request):
    return render(request,'home/innerpage/helpcenter.html')
def ccmgt(request):
    return render(request,'home/innerpage/cc-mgt.html')
def ccdetail(request):
    return render(request,'home/innerpage/cc-detail.html')
def deletefriend(request):
    Ac=request.session['userac']
    a=friend.objects.all()
    i=int(request.GET['id'])
    id=i-1
    a[id].delete()
    messages.error(request, '刪除好友成功')
    return redirect('/home/myfriends/')
def addfri1(request):
    Ac=request.session['userac']
    tel=request.GET['tel']
    a=member.objects.filter(memberTel=tel)
    membertel=a[0].memberTel
    membername=a[0].memberName
    memberImg=a[0].memberImg
    b=friend.objects.create(memberAc=Ac,friendTel=membertel,friendName=membername,friendImg=memberImg)
    b.save()
    messages.error(request, '新增好友成功')
    return redirect('/home/myfriends/')
def addfri(request):
    return render(request,'home/innerpage/addfri.html')
def addcc(request):
    return render(request,'home/innerpage/add-cc.html')
def authorized(request):
    return render(request,'home/authorized.html')
def car1_used(request):
    h=request.session['num']
    f=int(h)
    Ac=request.session['userac']
    c=car.objects.filter(memberAc=Ac)
    carName=c[f].carName
    carImg=c[f].carImg
    carNum=c[f].carNum
    carEv=c[f].carEv
    usetime2=int(request.GET['useTime'])
    time=60*usetime2
    return render(request,'home/car1_used.html',locals())
def car1(request):
    Ac=request.session['userac']
    a=int(request.GET['n'])
    b=a-1
    request.session['num']=b
    c=car.objects.filter(memberAc=Ac)
    carName=c[b].carName
    carImg=c[b].carImg
    carNum=c[b].carNum
    carEv=c[b].carEv
    carbrand=c[b].carbrand
    return render(request,'home/car1.html',locals())
def coupon(request):
    return render(request,'home/coupon.html')
def good1(request):
    return render(request,'home/good1.html')
def member_(request):
    if request.session['login']=='y':
        Ac=request.session['userac']
        n=friend.objects.all().count()
        r1=member.objects.get(memberAc=Ac)
        name=r1.memberName
        log=True
        return render(request,'home/member.html',locals())
    else:
        log=False
        return render(request,'home/memmber.html',locals())
def payment(request):
    return render(request,'home/payment.html')
def paymentpwd(request):
    return render(request,'home/paymentpwd.html')
def pet(request):
    return render(request,'home/pet.html')
def settings(request):
    return render(request,'home/settings.html')
def shop(request):
    point=request.session['point']
    return render(request,'home/shop.html',locals())
def garage(request):
    point=request.session['point']
    cars=car.objects.all()
    return render(request,'home/garage.html',locals())
def car1_confirm(request):
    h=request.session['num']
    f=int(h)
    point=request.session['point']
    Ac=request.session['userac']
    c=car.objects.filter(memberAc=Ac)
    carName=c[f].carName
    carImg=c[f].carImg
    carNum=c[f].carNum
    carEv=c[f].carEv
    d=int(c[f].carEv)
    usetime=str(request.GET['useTime'])
    usetime2=int(request.GET['useTime'])
    a=math.ceil(d*usetime2/1000)
    usepoint=str(a)
    return render(request,'home/car1_confirm.html',locals())
def mystoreaddcar(request):
    hf="../garage/"
    img="img/maserati1.jpg"
    name="汽車"
    a=myshop.objects.filter(href=hf,shopimg=img,shopName=name)
    if a.exists():
        a.delete()
        messages.error(request,'已從我的最愛中移除')
        return render(request,'home/shop.html',locals())
    else:
        add=myshop.objects.create(href=hf,shopimg=img,shopName=name)
        add.save()
        messages.error(request,'已將汽車加入我的最愛')
        return render(request,'home/shop.html',locals())
def modifymem1(request):
    name=request.GET['name']
    pw=request.GET['pw']
    tel=request.GET['tel']
    email=request.GET['email']
    adr=request.GET['adr']
    Ac=request.session['userac']
    a=member.objects.filter(memberAc=Ac).update(memberName=name,memberPw=pw,memberTel=tel,memberEml=email,memberAdr=adr)
    messages.error(request,'會員資料修改成功')
    return render(request,'home/index.html',locals())
def addconsume(request):
    Ac=request.session['userac']
    conName=request.GET['shopname']
    pie=request.GET['pice']
    b=int(pie)
    c=int(request.GET['a'])
    totalpoint=b*c
    a=consume.objects.create(memberAc=Ac,consumeName=conName,piece=pie,usePt=totalpoint)
    a.save()
    user=member.objects.filter(memberAc=Ac)
    point=user[0].memberPt-totalpoint
    d=member.objects.filter(memberAc=Ac).update(memberPt=point)
    request.session['point']=point
    messages.error(request,'成功兌換'+conName)
    return redirect('/home/pointrecord/')
def check(request):
    request.session['check']='y'
    Ac=request.session['userac']
    a=member.objects.get(memberAc=Ac)
    p=a.memberPt+5
    b=member.objects.filter(memberAc=Ac).update(memberPt=p)
    request.session['point']=p
    return redirect('/home/index/')
