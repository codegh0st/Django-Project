from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
# def learn_django(request):
#     return HttpResponse('hello django')
# def learn_python(request):
#     return HttpResponse('hello python')

from django.shortcuts import render
def learn_django(request):
    return render(request, 'course.html')

def learn_python(request):
    return render(request, 'course1.html')
