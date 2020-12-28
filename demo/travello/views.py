from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(req):

    dests= Destination.objects.all()
    return render(req, 'index.html',{'dests' : dests})

