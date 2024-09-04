from django.shortcuts import render
import datetime
# Create your views here.
def temp_v(request):
    date = datetime.datetime.now()
    my_dict = {'Date_msg':date}
    return render(request, 'testapp/index.html',context=my_dict)