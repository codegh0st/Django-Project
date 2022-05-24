from django.shortcuts import render
from django.http import HttpResponse

def fees_django(request):
    return HttpResponse('fees_django func inside fees: 300rs.')

def fees_python(request):
    return HttpResponse('fees_python func inside fees: 500rs.')