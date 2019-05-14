
from django.contrib import admin
from . import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'email' , 'phone']
     
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Attendance)

