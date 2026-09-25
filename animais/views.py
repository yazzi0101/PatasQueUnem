from django.shortcuts import render, redirect
from .models import Animal, InteresseAdocao
from .forms import AnimalForm, AdotanteForm


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

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def detalhes_animal(request, id):
    animal = Animal.objects.get(
        id=id,
        status='aprovado',
        adotado=False
    )

    return render(
        request,
        'detalhes_animal.html',
        {'animal': animal}
    )
    
def adotar_animal(request, id):

    animal = Animal.objects.get(
        id=id,
        status='aprovado',
        adotado=False
    )

    if request.method == 'POST':
        form = AdotanteForm(request.POST)

        if form.is_valid():
            adotante = form.save()

            InteresseAdocao.objects.create(
                adotante=adotante,
                animal=animal
            )

            return redirect('sucesso_adocao')

    else:
        form = AdotanteForm()

    return render(
        request,
        'adotar_um.html',
        {
            'form': form,
            'animal': animal
        }
    )