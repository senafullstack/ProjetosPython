from django.db import models
class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    datanasc = models.DateField()
    email =models.CharField(max_length=255,null=False)
    rua = models.CharField(max_length=120)
    cep = models.CharField(max_length=20)
    estado =  models.CharField(max_length=20)
    cidade =  models.CharField(max_length=80)
    bairro =  models.CharField(max_length=80)
    numero =  models.CharField(max_length=20)
    class Meta:
        db_table = 'clientes'
