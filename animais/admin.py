
from django.contrib import admin
from .models import Animal, Adotante, InteresseAdocao


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'sexo', 'idade', 'status', 'adotado')
    list_filter = ('status', 'adotado', 'especie')
    search_fields = ('nome', 'especie')


@admin.register(Adotante)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone', 'cidade', 'estado')
    search_fields = ('nome_completo', 'email', 'telefone')
    list_filter = ('cidade', 'estado')


@admin.register(InteresseAdocao)
class InteresseAdocaoAdmin(admin.ModelAdmin):
    list_display = ('adotante', 'animal')
    search_fields = ('adotante__nome_completo', 'animal__nome')
