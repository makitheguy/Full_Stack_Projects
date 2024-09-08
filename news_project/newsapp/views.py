from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')

def sports(request):
    return render(request, 'testapp/sports.html')

def politics(request):
    return render(request, 'testapp/politics.html')

def bollywood(request):
    return render(request, 'testapp/bollywood.html')