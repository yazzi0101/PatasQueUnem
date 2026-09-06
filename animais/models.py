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
    
    
class Adotante(models.Model):

    TIPO_RESIDENCIA_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('sitio', 'Sítio/Chácara'),
        ('outro', 'Outro'),
    ]

    ROTINA_CHOICES = [
        ('trabalho', 'Trabalho'),
        ('estudo', 'Estudo'),
        ('trabalho_estudo', 'Trabalho e estudo'),
        ('casa', 'Fico principalmente em casa'),
        ('outro', 'Outro'),
    ]

    TEMPO_SOZINHO_CHOICES = [
        ('menos_2', 'Menos de 2 horas'),
        ('2_4', 'De 2 a 4 horas'),
        ('4_8', 'De 4 a 8 horas'),
        ('mais_8', 'Mais de 8 horas'),
    ]

    CONVIVENCIA_CHOICES = [
        ('tranquila', 'Tranquila'),
        ('dificuldade', 'Possuem dificuldade de convivência'),
        ('nao_sei', 'Não sei informar'),
    ]

    RESTRICAO_CHOICES = [
        ('nao', 'Não'),
        ('sim', 'Sim'),
        ('nao_sei', 'Não sei'),
    ]

    nome_completo = models.CharField(
        max_length=150,
        verbose_name='Nome completo'
    )

    data_nascimento = models.DateField(
        verbose_name='Data de nascimento'
    )

    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone'
    )

    email = models.EmailField(
        verbose_name='E-mail'
    )

    cep = models.CharField(
        max_length=9,
        verbose_name='CEP'
    )

    endereco = models.CharField(
        max_length=200,
        verbose_name='Endereço'
    )

    tipo_residencia = models.CharField(
        max_length=20,
        choices=TIPO_RESIDENCIA_CHOICES,
        verbose_name='Tipo de residência'
    )

    com_quem_mora = models.CharField(
        max_length=200,
        verbose_name='Com quem mora'
    )

    residencia_segura = models.BooleanField(
        verbose_name='A residência é segura e adequada para receber o animal?'
    )

    restricao_animais = models.CharField(
        max_length=10,
        choices=RESTRICAO_CHOICES,
        verbose_name='A residência possui alguma restrição para animais?'
    )

    possui_outros_animais = models.BooleanField(
        default=False,
        verbose_name='Possui outros animais?'
    )

    quais_animais = models.TextField(
        blank=True,
        verbose_name='Quais animais possui e quantos?'
    )

    convivencia_animais = models.CharField(
        max_length=20,
        choices=CONVIVENCIA_CHOICES,
        blank=True,
        verbose_name='Como é a convivência com outros animais?'
    )

    rotina = models.CharField(
        max_length=20,
        choices=ROTINA_CHOICES,
        verbose_name='Como é sua rotina?'
    )

    tempo_sozinho = models.CharField(
        max_length=10,
        choices=TEMPO_SOZINHO_CHOICES,
        verbose_name='Por quanto tempo o animal ficaria sozinho?'
    )

    pessoa_apoio = models.TextField(
        verbose_name='Quem poderia ajudar em caso de necessidade?'
    )

    motivo_adocao = models.TextField(
        verbose_name='Por que deseja adotar um animal?'
    )

    experiencia_anterior = models.BooleanField(
        verbose_name='Já teve algum animal anteriormente?'
    )

    preferencia_animal = models.TextField(
        blank=True,
        verbose_name='Preferência ou características desejadas'
    )

    aceita_responsabilidades = models.BooleanField(
        verbose_name='Está de acordo com as responsabilidades da adoção?'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome_completo


class InteresseAdocao(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ]

    adotante = models.ForeignKey(
        Adotante,
        on_delete=models.CASCADE,
        related_name='interesses'
    )

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='interesses_adocao'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    def __str__(self):
        return f'{self.adotante.nome_completo} - {self.animal.nome}'