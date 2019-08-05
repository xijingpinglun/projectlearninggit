from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def index(request):
    return HttpResponse('nihao')



def hello(request):
    return HttpResponse('hello')


def list_user(request):
    users=User.objects.all()
    print(users)
    return render(request,'templates/list.html',{'users':users})