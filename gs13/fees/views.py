from django.shortcuts import render

# Create your views here.
def fees_python(request):
    dict_detail = {
        'nm':'Rahul',
        'roll':'400',
        'addr':'bihar',
    }
    dict2 = {
        'nm':'rahul',
        'rl':'101'
    }
    return render(request, 'fees/fees.html', dict2)