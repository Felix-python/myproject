from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return Httpresponse("index")


def login(request):
    return redirect('/index')
