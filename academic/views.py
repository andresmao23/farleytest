from django.shortcuts import render
from django.http import HttpResponse
from academic.models import Estudent, Enroll

#def index(request):
#    context = {}
#    return render(request, 'academic/index.html', context)

def index(request):
    student = Estudent.objects.get(id=1)
    enrolls = Enroll.objects.filter(estudent_id=1)
    context = {'student':student, 'enrolls':enrolls}
    return render(request, 'academic/index.html', context)