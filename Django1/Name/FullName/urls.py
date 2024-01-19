from django.urls import path
from FullName import views 

urlpatterns =[
    path('firstname/', views.firstname),
    path('middlename/', views.middlename) ,
]