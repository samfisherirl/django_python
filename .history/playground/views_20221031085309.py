from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request => response

def say_hello(request):
  # pull data and other stuff
  return render(request, 'hello.html')

