from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5+6
    return render(request, 'about.html', {'greting' : a})

def home(request):
    return HttpResponse('This is home page')