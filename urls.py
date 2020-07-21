from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.bmipage,name="bmipage"),
    path('check',views.getdata,name="getdata"),
