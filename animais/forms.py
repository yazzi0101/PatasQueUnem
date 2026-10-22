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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nome, campo in self.fields.items():
            if nome not in (
                'quais_animais',
                'possui_outros_animais',
                'aceita_responsabilidades',
            ):
                campo.required = True


    validador_telefone = RegexValidator(
        regex=r'^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$',
        message="Digite um telefone válido com DDD. Ex: (11) 91234-5678"
    )

    telefone = forms.CharField(
        validators=[validador_telefone],
        label='Telefone para contato',
        widget=forms.TextInput(
            attrs={'placeholder': '(11) 91234-5678'}
        )
    )

    email = forms.EmailField(
        label='E-mail para contato',
        error_messages={
            'invalid': 'Digite um endereço de e-mail válido.'
        }
    )

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
            'aceita_responsabilidades',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'residencia_segura': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Conte como sua residência é protegida e adequada para receber o animal.'
                }
            ),
            'convivencia_animais': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Explique como pretende apresentar o novo animal aos animais que já vivem com você.'
                }
            ),
            'pessoa_apoio': forms.Textarea(
                attrs={'rows': 3}
            ),
            'motivo_adocao': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

    def clean_aceita_responsabilidades(self):
        aceita = self.cleaned_data.get('aceita_responsabilidades')

        if not aceita:
            raise forms.ValidationError(
                'Você precisa concordar com as responsabilidades da adoção para continuar.'
            )

        return aceita

    def clean_nome_completo(self):
        nome = self.cleaned_data.get('nome_completo', '').strip()

        partes = nome.split()

        if len(partes) < 2:
            raise forms.ValidationError(
                'Digite seu nome completo, incluindo pelo menos o nome e o sobrenome.'
            )

        import re

        padrao = r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’-][A-Za-zÀ-ÖØ-öø-ÿ]+)*"

        if not all(re.fullmatch(padrao, parte) for parte in partes):
            raise forms.ValidationError(
                'Digite um nome válido, sem números ou caracteres especiais indevidos.'
            )

        return nome

        
    def clean(self):
        cleaned_data = super().clean()

        possui_outros = cleaned_data.get('possui_outros_animais')
        quais_animais = cleaned_data.get('quais_animais', '').strip()

        if possui_outros and not quais_animais:
            self.add_error(
                'quais_animais',
                'Informe quais animais vivem com você.'
            )

        return cleaned_data
