from django.shortcuts import render
from testapp.models import noida
# Create your views here.
def home(request):

    return render(request, 'testapp/home.html')

def noidaj(request):
    jobs_list = noida.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testapp/noida.html', context=my_dict)

def delhij(request):
    return render(request, 'testapp/delhi.html')

def gurugramj(request):
    return render(request, 'testapp/gurugram.html')