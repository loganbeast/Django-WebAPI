from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(req):

    dest1 = Destination()

    return render(req, 'index.html',{'dest1' : dest1})

