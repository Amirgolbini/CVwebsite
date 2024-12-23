from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    context = {'name': 'امیرحسین گلبینی مفرد', }

    return render(request, "website/index.html",context)


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    return render(request, "website/contact.html")
