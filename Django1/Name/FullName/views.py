from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstname(request):
    return render(request,'firstname.html')

def middlename(request):
    return render(request,'middlename.html')

