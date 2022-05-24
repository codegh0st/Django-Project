
from django.db import models
# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField(default=000)
    stuname = models.CharField(max_length=70, default='NA')
    stumail = models.EmailField(max_length=70, default='NA')
    stupass = models.CharField(max_length=70, default='NA')
    # appending 'comment', again have to run makemigraion then migrate command. then change will take effect
    commnet = models.CharField(max_length=40, default='comment not available')