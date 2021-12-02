from django.db import models
from django.db.models.deletion import CASCADE

class Clientes(models.Model):
    estado_civil_escolha = [
        ('Feminino',(
                ('sta', 'Solteira'),
                ('csa', 'Casada'),
                ('vva', 'Viúva'),
                ('dva', 'Divorciada'),
            )
        ),
        ('Masculino', (
                ('st', 'Solteiro'),
                ('cs', 'Casado'),
                ('vv', 'Viúvo'),
                ('dv', 'Divorciado'),
            )
        ),
    ]
    sexo_escolha = [
        ('fm', 'Feminino'),
        ('ms', 'Masculino'),
    ]
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos/', blank=True)
    obs = models.TextField(max_length=400, default="Nenhuma", blank=True)
    endereco = models.CharField(max_length=300)
    cep = models.TextField(max_length=9)
    sexo = models.TextField(max_length=2, choices=sexo_escolha, default='fm')
    estado_civil = models.TextField(max_length=3, choices=estado_civil_escolha, default='sta')
    email = models.EmailField()
    rg = models.TextField(max_length=12, blank=False)
    cpf = models.TextField(max_length=14, blank=False)

    def __str__(self):
        return self.nome

class Anamnese(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=CASCADE, blank=False)
    altura = models.FloatField(max_length=4, blank=False)
    peso = models.FloatField(max_length=7, blank=False)
    fumante = models.BooleanField(default=False)
    bebe = models.BooleanField(default=False)
    filhos = models.BooleanField(default=False)
    filhos_qt = models.IntegerField(default=0)
    cirurgia = models.BooleanField(default=False)
    cirurgia_txt = models.CharField(max_length=100, blank=True)
    tratamento_estetico = models.BooleanField(default=False)
    tratamento_estetico_txt = models.CharField(max_length=200, blank=True)
    tratamento_medico = models.BooleanField(default=False)
    tratamento_medico_txt = models.CharField(max_length=200, blank=True)
    tratamento_ortomolecular = models.BooleanField(default=False)
    tratamento_ortomolecular_txt = models.CharField(max_length=150, blank=True)
    alergia = models.BooleanField(default=False)
    alergia_txt = models.CharField(max_length=100, blank=True)
    atividade_fisica = models.BooleanField(default=False)
    atividade_fisica_txt = models.CharField(max_length=150, blank=True)
    intestino_regular = models.BooleanField(default=True)
    ingestao_liquido = models.BooleanField(default=False)
    ingestao_liquido_txt = models.CharField(max_length=100, blank=True)
    gestante = models.BooleanField(default=False)
    hipertensao = models.BooleanField(default=False)
    epilepsia = models.BooleanField(default=False)
    problema_ortopedico = models.BooleanField(default=False)
    problema_ortopedico_txt = models.CharField(max_length=150, blank=True)
    problema_oncologico = models.BooleanField(default=False)
    problema_oncologico_txt = models.CharField(max_length=150, blank=True)
    usa_acido = models.BooleanField(default=False)
    usa_acido_txt = models.CharField(max_length=100, blank=True)
    usa_produtos = models.BooleanField(default=False)
    usa_produtos_txt = models.CharField(max_length=200, blank=True)
    usa_marcapasso = models.BooleanField(default=False)
    usa_metais = models.BooleanField(default=False)
    usa_metais_txt = models.CharField(max_length=100, blank=True)
    usa_anticonsepcional = models.BooleanField(default=False)
    usa_anticonsepcional_txt = models.CharField(max_length=100, blank=True)
    menstruacao_regular = models.BooleanField(default=True)
    lesoes = models.BooleanField(default=False)
    lesoes_txt = models.CharField(max_length=150, blank=True)
    varizes = models.BooleanField(default=False)
    varizes_txt = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente.nome