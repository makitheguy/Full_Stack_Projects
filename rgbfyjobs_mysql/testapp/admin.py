from django.contrib import admin
from testapp.models import noida,delhi,gurugram,mumbai
# Register your models here.
class noidaadmin(admin.ModelAdmin):
    list_display = ['date','title','company','eligibility','address','email','phonenumber']

class delhiadmin(admin.ModelAdmin):
    list_display = ['date','title','company','eligibility','address','email','phonenumber']

class gurugramadmin(admin.ModelAdmin):
    list_display = ['date','title','company','eligibility','address','email','phonenumber']

class mumbaiadmin(admin.ModelAdmin):
    list_display = ['date','title','company','eligibility','address','email','phonenumber']

admin.site.register(noida,noidaadmin)
admin.site.register(delhi,delhiadmin)
admin.site.register(gurugram,gurugramadmin)
admin.site.register(mumbai,mumbaiadmin)