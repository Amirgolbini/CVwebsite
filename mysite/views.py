from django.shortcuts import HttpResponse

def http_test(request):
    return HttpResponse("Hello")