from json import detect_encoding
from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    fm.order_fields(field_order = ['email','first_name', 'name'])
    return render(request, 'enroll/user_registration.html', {'form':fm})

# order_fields fuction ek list leta hai as argvmnt is list me ham form field ka name pass kr 
# dete hai. jis order order me list pass karte hai usi order me templete me render ho kar dikhta hai.
# fm ek object hai jo StudentRegistration class se bana hai. isi par ye function apply hota hai
