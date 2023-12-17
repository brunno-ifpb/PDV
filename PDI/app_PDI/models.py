from django.db import models

# Create your models here.

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)

    nome = models.TextField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    validade = models.TextField()
    lucro = models.IntegerField()
    lot = models.IntegerField()
    img = models.ImageField()

class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)

    # Campos de identificação pessoal
    foto_pessosal = models.ImageField()
    nome = models.TextField(max_length=255)
    CPF = models.TextField(max_length=255)
    RG = models.TextField(max_length=255)
    PIS_Pasep = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    #titulo_eleitor = models.ImageField()
    comprovante_residencia = models.ImageField()
    comprovante_escolaridade = models.ImageField()
    
    # Campos de emprego
    curriculo = models.ImageField()
    CTPS = models.CharField(max_length=255)  # carteira de trabalho
    cargo = models.TextField(max_length=255)
    salario = models.IntegerField()
    efetivado = models.DateField()
    departamento = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)

    # Campos de contato
    endereco = models.TextField(max_length=255)
    numero_contato1 = models.CharField(max_length=15)
    numero_contato2 = models.CharField(max_length=15, blank=True, null=True)
    Email = models.EmailField()

    # Campo de senha
    senha = models.CharField(max_length=255)


#RG, CPF, título de eleitor, comprovante de residência, comprovante de escolaridade, inscrição no PIS/Pasep, carteira de trabalho (CTPS)


