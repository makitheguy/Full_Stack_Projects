from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['eno','ename', 'esal','eaddr']

admin.site.register(Employee,EmpAdmin)