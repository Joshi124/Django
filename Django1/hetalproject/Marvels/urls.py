from django.urls import path
from Marvels import views 

urlpatterns =[
    path('spiderman/', views.spiderman),
    path('ironman/', views.ironman) ,
]
