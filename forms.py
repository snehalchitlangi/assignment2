from django import forms

class MyForms(forms.Form):
    weight=forms.CharField(label="weight",max_length=100)
    height=forms.CharField(label="height",max_length=100) 
