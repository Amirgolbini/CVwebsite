from django.urls import path
from website.views import *

urlpatterns = [
    path('http-test/', http_test)
]
