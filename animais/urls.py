from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path(
        'animais/',
        views.animais_disponiveis,
        name='animais_disponiveis'
    ),
    
    path(
        'animal/<int:id>/',
        views.detalhes_animal,
        name='detalhes_animal'
    ),
    
    path(
        'colocar-animal/',
        views.colocar_adocao,
        name='colocar_adocao'
    ),
    
    path(
        'sucesso-cadastro/',
        views.sucesso_cadastro,
        name='sucesso_cadastro'
    ),
    
    path(
        'sobre-nos/',
        views.sobre_nos,
        name='sobre_nos'
    ),
    
    path(
    'adotar/<int:id>/',
    views.adotar_animal,
    name='adotar_animal'
    )
]
