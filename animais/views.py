from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm


def home(request):
    animais = Animal.objects.filter(
        status='aprovado',
        adotado=False
    )

    return render(request, 'home.html', {'animais': animais})


def animais_disponiveis(request):
    animais = Animal.objects.filter(
        status='aprovado',
        adotado=False
    )

    return render(request, 'adopt.html', {'animais': animais})


def colocar_adocao(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('sucesso_cadastro')

    else:
        form = AnimalForm()

    return render(request, 'colocar_adocao.html', {'form': form})

def sucesso_cadastro(request):
    return render(request, 'sucesso_cadastro.html')