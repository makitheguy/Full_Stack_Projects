from django.shortcuts import render
from testapp.models import Employee_info

# Create your views here.
def home(request):
    emp_list = Employee_info.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request, 'testapp/home.html',context=my_dict)