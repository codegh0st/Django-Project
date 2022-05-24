from django.contrib import admin
from enroll import models
# OR, from enroll.models import Student


# Register your models here.
admin.site.register(models.Student)
# OR, admin.site.registers(Student)