from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    s="<h1>Welcome to Django </h1>"
    return HttpResponse(s)