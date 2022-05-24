from multiprocessing import context
from django.shortcuts import render

# Create your views here.
# def base(request):
#     return render(request, 'core/base.html')


def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def about(request):
    context = {'about':'active'}
    return render(request, 'core/about.html', context)

def contact(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)