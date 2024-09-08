from django.contrib import admin
from testapp.models import Employee_info
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['ename', 'esal','eaddr']

admin.site.register(Employee_info,EmpAdmin)