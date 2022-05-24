from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_django(reguest):
    return HttpResponse("hello Learn_djanog function")

def learn_python(reguest):
    return HttpResponse("hello Learn_python function")

def learn_Math(reguest):
    a = 50+60
    return HttpResponse(f"hello Learn_math function{a}")
