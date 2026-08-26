# Create your models here.

from django.db import models

class Animal(models.Model):
    
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Femêa'),
    ]
    
    UNIDADE_IDADE_CHOICES = [
        ('meses','Meses'),
        ('anos','Anos'),
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
        choices=SEXO_CHOICES
    )
    
    descricao = models.TextField()
    adotado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
    
