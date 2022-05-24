from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def fees_django(request):
#     return HttpResponse('hello django fees 400rs')
# def fees_python(request):
#     return HttpResponse('hello python feess 500rs')

def fees_django(request):
    # yahan par python ka dusra logic likha ja sakta hai. render karne se pahle. 
    return render(request, 'fees.html')

def fees_python(request):
    # yahan par python ka dusra logic likha ja sakta hai. render karne se pahle. 
    return render(request, 'fees1.html')
