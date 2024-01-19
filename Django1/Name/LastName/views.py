from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lastname(request):
    return render(request,'lastname.html')


