from django.db import models
from .hoteldb import Hotel
 
class Hospede(models.Model):
      id_hospede = models.AutoField(primary_key=True)
      nome = models.CharField(max_length=80)
      foto = models.CharField(max_length=255)
      fone = models.CharField(max_length=20)
      email = models.CharField(max_length=255)
      cpf = models.CharField(max_length=80)
      datanasc = models.DateField()
      pai = models.CharField(max_length=80)
      mae = models.CharField(max_length=80)
      quarto = models.CharField(max_length=80)
      entrada =  models.DateField()
      saida = models.DateField()
      placa = models.CharField(max_length=80)
      marca = models.CharField(max_length=80)
      modelo = models.CharField(max_length=80)
      cor = models.CharField(max_length=80)
      hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,db_column="id_hotel")
 
      class Meta:
            db_table = 'hospede'
