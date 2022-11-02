from django.shortcuts import render

# Create your views here.
# request => response

def say_hello(requests):
  # pull data and other stuff
  return HttpResponse('Hello Worlds')

