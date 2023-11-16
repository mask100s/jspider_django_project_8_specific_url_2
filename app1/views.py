from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dosa(request):
  return HttpResponse('<h1>this http string response</h1>')
