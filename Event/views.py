from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    return render(request,'index.html')

def event(request):
    return render(request,'etemp/eindex.html')

