
from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.

def success(request):
  return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
      fm = StudentRegistration(request.POST)
      print('ye post request se aaya hai')
      print(request.POST) # form field ka value rahata jo post method se bheja gaya hai. 
      if fm.is_valid():
           print('name cleaned Data:', fm.cleaned_data['name'])
           print('email cleaned Data:', fm.cleaned_data['email'])
           nm = (request.POST['name']) # form ke data ko aise hi fech kiya ja sakta hai. 
           eml = (request.POST['email'])
           return HttpResponseRedirect('/enroll/successapp/')
          #  return render(request, 'enroll/success.html', {'user_name':nm}) # ye isi url enroll/enrollapp pe chalega.
          
          # agar aap aap chahte hai ki Success msg ke liye alag url dikhe to uske liye hame HttpRsponserRedirect
          # method use karna hota hai kisi url ko hti karane ke liye. iss line pe control ane pe defined
          # url pe automatic jayega. fir hame us url ke liye view.py me hi templete render karwana hota hai.
          
           
    
    else:
      fm = StudentRegistration()
      print('ye get request se aaya hai')
    # passing two dictionary same time one with key 'form', 2nd with key 'req' req containing value given by users in form
    return render(request, 'enroll/user_registration.html', {'form':fm, 'req':request.POST})
  
