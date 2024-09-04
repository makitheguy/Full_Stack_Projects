from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request , 'testapp/home.html')

def profile(request):
    return render(request,'testapp/profile.html')