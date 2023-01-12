from django.db import models

# Create your models here.
class member(models.Model):
    memberAc=models.CharField(max_length=10,null=False)
    memberPw=models.CharField(max_length=15,null=False)
    memberName=models.TextField(max_length=15,default="")
    memberTel=models.CharField(max_length=10,default="")
    memberEml=models.TextField(max_length=20,default="")
    memberAdr=models.TextField(max_length=25,default="")
    memberImg=models.CharField(max_length=20,default="img/member.png")
    create=models.DateTimeField(auto_now_add=True)
    memberPt=models.IntegerField(default=0)
    class Meta:
        db_table="member"
class bill(models.Model):
    billId=models.CharField(max_length=10,unique=True)
    memberId=models.CharField(max_length=10)
    totalMoney=models.IntegerField()
    cbTax=models.FloatField()
    cbPoint=models.FloatField()
    cbEm=models.FloatField()
    billDt=models.DateTimeField()
    class Meta:
        db_table="bill"
class car(models.Model):
    memberAc=models.CharField(max_length=10,default="")
    carName=models.CharField(max_length=10,default="")
    carImg=models.CharField(max_length=25,default="")
    carNum=models.CharField(max_length=10,default="")
    carEv=models.IntegerField(default=0)
    carbrand=models.CharField(max_length=15,default="")
    class Meta:
        db_table="car"
class consume(models.Model):
    memberAc=models.CharField(max_length=10,default="")
    consumeName=models.CharField(max_length=15,default="")
    carName=models.CharField(max_length=10,default="")
    carNum=models.CharField(max_length=10,default="")
    usePt=models.IntegerField(default=0)
    useSec=models.IntegerField(default=0)
    starttime=models.DateTimeField(auto_now=True)
    piece=models.IntegerField(default=0)
    class Meta:
        db_table="consume"
class myshop(models.Model):
    href=models.CharField(max_length=20,default="")
    shopimg=models.CharField(max_length=20,default="")
    shopName=models.CharField(max_length=20,default="")
    class Meta:
        db_table="myshop"
class friend(models.Model):
    memberAc=models.CharField(max_length=10,null=False)
    friendTel=models.CharField(max_length=10,default="")
    friendName=models.TextField(max_length=15,default="")
    friendImg=models.CharField(max_length=20,default="")
    class Meta:
        db_table="friend"