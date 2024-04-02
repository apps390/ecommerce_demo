from django.contrib import admin
from students.models import Students,details,CustomUser

admin.site.register(Students)
admin.site.register(details)
admin.site.register(CustomUser)