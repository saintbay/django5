from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(""" <h1>This is home page</h1> """)

def retrieve(request, id):
    return HttpResponse(f""" <h1>This is {id} retrieve page</h1> """)