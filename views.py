from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
# Create your views here.

def bmipage(request):
    f1=forms.MyForms()
    return render(request,"bmi.html",{'form':f1})

def getdata(request):
    if request.method=='GET':
         weight=request.GET['weight']   
         height=request.GET['height']
         w=float(weight)
         h=float(height)
         bmi=w/(h*h)
         return render(request,"calculate.html",{"weight":w,"height":h,"b1":bmi})
    if request.method=='POST':
         weight=request.POST['weight']   
         height=request.POST['height']
         w=float(weight)
         h=float(height)
         bmi=w/(h*h)
         return render(request,"calculate.html",{"weight":w,"height":h,"b1":bmi})
