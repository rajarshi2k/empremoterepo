from django.contrib import admin
from .models import Emp
class EmpAdmin(admin.ModelAdmin):
    list_display = ['name','age','basic']
# Register your models here.
admin.site.register(Emp,EmpAdmin)