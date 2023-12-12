from django.db import models
from .perfildb import Perfil
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    sexo = models.CharField(max_length=80)
    foto = models.CharField(max_length=255)
    foto64 = models.TextField()
    arquivo = models.CharField(max_length=255,null=True),
    campooculto = models.CharField(max_length=80)
    datanasc = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=14)    
    cep = models.CharField(max_length=30)    
    cnpj = models.CharField(max_length=30)    
    fone =  models.CharField(max_length=14)    
    ativo = models.BooleanField(default=False)
    cor = models.CharField(max_length=14)
    texto = models.TextField()
    idade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    textolongo = models.TextField()
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,db_column='id_perfil', null=True)
    class Meta:
        db_table ="cliente"