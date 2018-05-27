from django.conf.urls import url
from django.contrib import admin
from academic.views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
]
