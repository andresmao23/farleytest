from django.shortcuts import render
from django.http import HttpResponse
from academic.models import Estudent, Enroll

#def index(request):
#    context = {}
#    return render(request, 'academic/index.html', context)

def index(request):
    userid = request.user.id
    student = Estudent.objects.get(user_id=userid)
    enrolls = Enroll.objects.filter(estudent_id=student.id)
    context = {'student':student, 'enrolls':enrolls}
    return render(request, 'academic/index.html', context)