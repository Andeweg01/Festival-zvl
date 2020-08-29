from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tickets/', views.tickets, name='tickets'),
    path('sponsoring/', views.sponsoring, name='sponsoring'),
    path('media/', views.media, name='media'),
]
