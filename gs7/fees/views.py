from django.shortcuts import render
from django.http import HttpResponse

def fees_django(request):
    return HttpResponse('fees_Hello django')

def fees_python(request):
    return HttpResponse('fees_Hello python')
