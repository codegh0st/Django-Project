from django.shortcuts import render

# Create your views here.

def enroll(request):
    return render(request, 'enroll/studentinfo.html')