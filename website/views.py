from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse('About us')

def contact(request):
    return HttpResponse('Contact Us')
