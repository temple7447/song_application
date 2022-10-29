from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request ,'songs/index.html' )


def about(request):
    return HttpResponse("About page")


def songs(request):
    return HttpResponse("you are in the song page and you are welcome to this world")
