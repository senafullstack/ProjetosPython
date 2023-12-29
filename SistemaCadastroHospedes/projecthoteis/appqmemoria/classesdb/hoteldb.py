from django.db import models
 
class Hotel(models.Model):
      id_hotel = models.AutoField(primary_key=True)
      nome = models.CharField(max_length=80)
      nomefantasia = models.CharField(max_length=80)
      cnpj = models.CharField(max_length=80)
      endereco = models.CharField(max_length=80)
      numero = models.CharField(max_length=80)
      bairro = models.CharField(max_length=80)
      cidade = models.CharField(max_length=80)
      estado = models.CharField(max_length=80)
      responsavel = models.CharField(max_length=80)
      fone = models.CharField(max_length=80)
      email = models.CharField(max_length=255)
 
      class Meta:
            db_table = 'hotel'
