# from django.shortcuts import render

# # Create your views here.

# backend/blog/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello from blog app")
