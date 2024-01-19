from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def superman(request):
    return render(request,'superman.html')

def batman(request):
    return render(request,'batman.html')