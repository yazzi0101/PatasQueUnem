from django import forms
from django.core.validators import RegexValidator

from .models import Animal, Adotante


class AnimalForm(forms.ModelForm):
    validador_telefone = RegexValidator(
        regex=r'^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$',
        message="Digite um telefone válido com DDD. Ex: (11) 91234-5678"
    )
        
    telefone = forms.CharField(
        validators=[validador_telefone],
        label='Telefone para contato',
        widget=forms.TextInput(attrs={'placeholder': '(11) 91234-5678'})
    )
        
    email = forms.EmailField(
        label='E-mail para contato',
        error_messages={'invalid': 'Digite um endereço de e-mail válido.'}
    )
        
    class Meta:
        model = Animal
        fields = [
            'nome',
            'foto',
            'especie',
            'idade',
            'selecione',
            'sexo',
            'descricao',
            'motivo_doacao',
            'possui_problema_saude',
            'problema_saude',
            'telefone',
            'email',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'estado',
        ]

        labels = {
            'nome': 'Nome do animal',
            'foto': 'Foto do animal',
            'especie': 'Espécie',
            'idade': 'Idade',
            'selecione': 'Selecione',
            'sexo': 'Sexo',
            'descricao': 'Descrição',
            'motivo_doacao': 'Qual o motivo da doação?',
            'possui_problema_saude': 'Possui algum problema de saúde ou comorbidade?',
            'problema_saude': 'Se sim, qual?',
            'telefone': 'Telefone para contato',
            'email': 'E-mail para contato',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
        }

        # Redefine a opção vazia padrão do campo de seleção
        widgets = {
            'sexo': forms.Select(choices=[('', 'Selecione o sexo')] + list(Animal.SEXO_CHOICES)),
        }

class AdotanteForm(forms.ModelForm):

    class Meta:
        model = Adotante

        fields = [
            'nome_completo',
            'data_nascimento',
            'telefone',
            'email',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'estado',
            'tipo_residencia',
            'com_quem_mora',
            'residencia_segura',
            'restricao_animais',
            'possui_outros_animais',
            'quais_animais',
            'convivencia_animais',
            'rotina',
            'tempo_sozinho',
            'pessoa_apoio',
            'motivo_adocao',
            'experiencia_anterior',
            'preferencia_animal',
            'aceita_responsabilidades',
        ]