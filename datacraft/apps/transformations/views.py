from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from .models import Question

def index(request):
    #return HttpResponse("Path: transformations")
    return render(request, 'transformations/index.html')