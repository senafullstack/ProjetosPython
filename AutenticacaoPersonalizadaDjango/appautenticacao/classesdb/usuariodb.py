from django.db import models
from .perfildb import Perfil
from .departamentodb import Departamento
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    datanasc = models.DateField()
    email =models.CharField(max_length=255,null=False)
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,db_column='id_perfil')
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,db_column='id_departamento',null=True)
    senha = models.CharField(max_length=255)
    class Meta:
        db_table = 'usuario'