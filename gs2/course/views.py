from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def learndj(request):
    return HttpResponse('<h1>hello dango my 2nd function</h2>')

def learnpy(request):
    return HttpResponse('<h1> learn python</h2>')

def learnvar(request):
    a = 20+50;
    return HttpResponse(a)

def learnf(request):
    f='geekyshow'
    return HttpResponse(f'i am learning django with :{f}')