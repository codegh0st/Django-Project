from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField(default=000)
    stuname = models.CharField(max_length=70, default='NA')
    stumail = models.EmailField(max_length=70, default='NA')
    stupass = models.CharField(max_length=70, default='NA')
    def __str__(self):
        return self.stuname, self.stumail
    """ --str--(self): function return karta hai iske andar ka table Studends
    ka ek field ka value . ye database se us field ko value lega aur return kr dega, 
    ye hame admin site me dekhne ko milega. ye string return karta hai to jab aap koi interger value 
    ko return karwa rahe hai to error dega, is integer value ko intermer me typecast karna padega 
    return str(self.stuid)"""