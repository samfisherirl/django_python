from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request => response

def say_hello(request):
  # pull data and other stuff
  x = 1
  y = 2
  return render(request, 'hello.html', { 'name': 'John', 'x': x, 'y': y })

