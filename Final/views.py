from django.shortcuts import render , redirect, HttpResponse
from .models import *
from .forms import *

# Create your views here.

def inicio (request):
    return render (request, 'inicio.html')