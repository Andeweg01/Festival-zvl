from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_concerts, name='concerts'),
    path('<concert_id>', views.concert_detail, name='concert_detail'),
]
