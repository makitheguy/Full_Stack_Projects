from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
# Create your views here.
def home(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request, 'testapp/home.html',my_dict)