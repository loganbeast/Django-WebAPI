from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return render(req, 'home.html', {'name': 'Son'})


def result(req):

    val1 = req.POST['number1']
    val2 = req.POST['number2']
    res = int(val1) + int(val2)

    return render(req, 'result.html', {'result': res})
