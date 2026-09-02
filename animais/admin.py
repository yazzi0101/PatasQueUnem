
# Register your models here.

from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'sexo', 'idade', 'status', 'adotado')
    list_filter = ('status', 'adotado', 'especie')
    search_fields = ('nome', 'especie')