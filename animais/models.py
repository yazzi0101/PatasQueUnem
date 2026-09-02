# Create your models here.

from django.db import models

class Animal(models.Model):
    
    SEXO_CHOICES = [
        ('', 'Selecione o sexo'),
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    
    UNIDADE_IDADE_CHOICES = [
        ('meses','Meses'),
        ('anos','Anos'),
    ]    
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ]
    
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='animais/')
    especie = models.CharField(max_length=50)
    idade = models.PositiveBigIntegerField()
    
    selecione= models.CharField(
        max_length=10,
        choices=UNIDADE_IDADE_CHOICES,
        default='anos'
    )
    
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        default=''
    )
    
    descricao = models.TextField()
    

    motivo_doacao = models.TextField(
        blank=True,
        verbose_name='Motivo da doação'
    )

    possui_problema_saude = models.BooleanField(
        default=False,
        verbose_name='Possui problema de saúde ou comorbidade?'
    )

    problema_saude = models.TextField(
        blank=True,
        verbose_name='Qual problema de saúde ou comorbidade?'
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Telefone para contato'
    )

    email = models.EmailField(
        blank=True,
        verbose_name='E-mail para contato'
    )

    endereco = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Endereço'
    )

    cep = models.CharField(
    max_length=9,
    blank=True,
    default='',
    verbose_name='CEP'
)

    bairro = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Bairro'
    )

    cidade = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Cidade'
    )

    estado = models.CharField(
        max_length=2,
        blank=True,
        verbose_name='Estado'
    )

    adotado = models.BooleanField(default=False) 
        
    status = models.CharField(
     max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    
    def __str__(self):
        return self.nome