from django.shortcuts import render
from django.http import HttpResponse
def index(response):
    return HttpResponse("hello")

# Create your views here.
