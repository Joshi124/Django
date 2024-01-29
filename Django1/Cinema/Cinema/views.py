from django.shortcuts import render
from django.http import HttpResponse
from .models import Cinemas
# Create your views here.
def cinema(request):
     picture = Cinemas.objects.all()
     return render(request,'films.html',{'film' :picture})
