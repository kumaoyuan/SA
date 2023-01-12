"""SA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import memberViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'memberdata',memberViewSet,basename='member')
urlpatterns=router.urls

urlpatterns += [
    path("",views.toindex),
    path("index/",views.index),
    path('welcome/',views.hello),
    path('signup1/',views.signup1),
    path('signup/',views.signup),
    path('pointrecord/',views.pointrecord),
    path('petwarehouse/',views.petwarehouse),
    path('perconsent/',views.perconsent),
    path('noticenter/',views.noticenter),
    path('mystore/',views.mystore),
    path('mypet/',views.mypet),
    path('myfriends/',views.myfriends),
    path('mycoupon/',views.mycoupon),
    path('addcar/',views.addcar),
    path('modifymem/',views.modifymem),
    path('login/',views.login),
    path('login1/',views.login1),
    path('logout/',views.logout),
    path('leaderboard/',views.leaderboard),
    path('helpcenter/',views.helpcenter),
    path('ccmgt/',views.ccmgt),
    path('ccdetail/',views.ccdetail),
    path('addfri/',views.addfri),
    path('addcc/',views.addcc),
    path('authorized/',views.authorized),
    path('car1_used/',views.car1_used),
    path('car1/',views.car1),
    path('coupon/',views.coupon),
    path('good1/',views.good1),
    path('member/',views.member_),
    path('payment/',views.payment),
    path('paymentpwd/',views.paymentpwd),
    path('pet/',views.pet),
    path('settings/',views.settings),
    path('shop/',views.shop),
    path('garage/',views.garage),
    path('car1_confirm/',views.car1_confirm),
    path('consume1/',views.consume1),
    path('mystoreaddcar/',views.mystoreaddcar),
    path('modifymem1/',views.modifymem1),
    path('addconsume/',views.addconsume),
    path('addfri1/',views.addfri1),
    path('deletefriend/',views.deletefriend),
    path('addcar1/',views.addcar1),
    path('check/',views.check),
]
