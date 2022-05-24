from django.shortcuts import render

# Create your views here.
def learn_django(request):
    my_dict = {
        'stu1': {'nm':'rahul', 'rl':100},
        'stu2': {'nm:':'suresh', 'rl':101}, 
        'stu3': {'nm:':'mahesh', 'rl':102}, 
    }
    students = {'student': my_dict}
    return render(request, 'course/course.html', students)