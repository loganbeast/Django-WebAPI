from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(req):

    dest1 = Destination(1,'Mumbai',"destination_1.jpg","This is fucking beautiful place",990,False)
    dest2 = Destination(2,'Ha Noi',"destination_2.jpg","Best place for couple",990,True)
    dest3 = Destination(3,'Okinawa',"destination_3.jpg","There is a good place for single boy",990,True)

    dests = [dest1,dest2,dest3]

    return render(req, 'index.html',{'dests' : dests})

