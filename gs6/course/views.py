from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('learn_django inside course.view')
def learn_python(request):
    return HttpResponse('learn pyhton func inside course.view')
