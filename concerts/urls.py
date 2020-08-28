from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_concerts, name='concerts'),
    path('<int:concert_id>/', views.concert_detail, name='concert_detail'),
    path('add/', views.add_concert, name='add_concert'),
    path('edit/<int:concert_id>/', views.edit_concert, name='edit_concert'),
]
