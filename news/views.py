from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(request)
    return HttpResponse('HEllo')


def test(request):
    return  HttpResponse('<h1> TWSSSSSSSSSSSSSSSSSSSS </h1>')