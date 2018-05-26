from django.contrib import admin
from academic.models import Estudent, Teacher, Subject, Enroll
# Register your models here.
admin.site.register(Estudent)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Enroll)
