from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animais/', views.animais_disponiveis, name='animais_disponiveis'),
    path('colocar-animal/', views.colocar_adocao, name='colocar_adocao'),
    path('sucesso-cadastro/', views.sucesso_cadastro, name='sucesso_cadastro'),
]
