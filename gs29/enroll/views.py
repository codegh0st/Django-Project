from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration(auto_id='some_%s', label_suffix='?', initial={'name':'Rahul', 'email':'rahul@gamil.com'})
    return render(request, 'enroll/user_registration.html', {'form':fm})

# # auto_id = 'some_%s' -- aisa likhne se field ka name forms.py jo likhe the woh %s ke jagah par l
# # le leta hai.
# auto_id = True ye field ka naem le leta hai.
# auto_id = False ye id attribute ko hi remove kar deta hai.
# auto_id = 'any string ' ye True ke jisa hi name ko leta hai. jo from.py file me defiene krete hai.

# label_suffix = '-' is single qoutes ke andar jo bhi denge woh label le suffix me dikhega
# default me colon dikhta hai e.g Name: or Email: we can replace colon with any other charector.
# fm = StudentRegistration(auto_id='some_%s', label_suffix='-')
# fm ek object create huwa jo dictionary ke tarah users_regstraion.html file me pass hokar jayega.

# initial = {'name':'rahul'}, ye initial value form me phale se bhara hua rahega. 