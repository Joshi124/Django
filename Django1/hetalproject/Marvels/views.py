from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def spiderman(request):
    return render(request,'spiderman.html')

def ironman(request):
    return render(request,'ironman.html')