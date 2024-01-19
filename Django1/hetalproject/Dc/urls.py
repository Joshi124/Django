from django.urls import path
from Dc import views

urlpatterns=[
    path('batman/', views.batman),
    path('superman/', views.superman),
]
    