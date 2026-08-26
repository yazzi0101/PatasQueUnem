from django.shortcuts import render
from .models import Animal


def home(request):
    animais = Animal.objects.filter(adotado=False)

    return render(request, 'home.html', {'animais': animais})