from django.contrib import admin
from enroll import models
# Register your models here.

# using decorator to rgister our tables/models 
# if decorator used this line not needed : admin.site.register(models.Student, StudentAdmin) as given below
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stumail', 'stupass')
    
# admin.site.register(models.Student, StudentAdmin)