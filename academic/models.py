from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Estudent(models.Model):
    GENRES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    genre = models.CharField(max_length=1, choices=GENRES, default='M')

    def __unicode__(self):
        return self.name + ' ' + self.last_name


class Teacher(models.Model):
    GENRES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    genre = models.CharField(max_length=1, choices=GENRES, default='M')

    def __unicode__(self):
        return self.name + ' ' + self.last_name


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    teacher = models.ManyToManyField(Teacher, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Enroll(models.Model):
    estudent = models.ForeignKey(Estudent, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    first_note = models.FloatField(default=0)
    second_note = models.FloatField(default=0)
    def_note = models.FloatField(default=0)

    class Meta:
        unique_together = ('estudent', 'subject',)