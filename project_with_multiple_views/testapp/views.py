from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mumbai(request):
    return HttpResponse('<h1>this is from mumbai</h1>')
def delhi(request):
    return HttpResponse('<h1>this is from delhi</h1>')
def noida(request):
    return HttpResponse('<h1>this is from noida</h1>')
def gurugram(request):
    return HttpResponse('<h1>this is from gurugram</h1>')