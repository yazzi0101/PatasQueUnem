from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('animais/', views.animais_disponiveis, name='animais_disponiveis'),
]
