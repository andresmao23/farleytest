from __future__ import unicode_literals

from django.db import models

class Estudent(models.Model):
    GENRES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
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
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    genre = models.CharField(max_length=1, choices=GENRES, default='M')

    def __unicode__(self):
        return self.name + ' ' + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Enroll(models.Model):
    estudent = models.ForeignKey(Estudent, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    first_note = models.FloatField(default=0)
    second_note = models.FloatField(default=0)
    final_note = models.FloatField(default=0)

    class Meta:
        unique_together = ('estudent', 'subject',)