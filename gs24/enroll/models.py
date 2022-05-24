from django.db import models

# Create your models here.
class Student(models.Model):
    studi = models.IntegerField(default=000)
    stuname = models.CharField(max_length=70, null=True)
    stumail = models.EmailField(max_length=40, null=True)
    stupass = models.CharField(max_length=70, null=True)