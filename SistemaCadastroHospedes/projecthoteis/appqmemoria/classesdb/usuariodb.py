from django.db import models
from .departamentodb import Departamento
from .hoteldb import Hotel
from .perfildb import Perfil
 
class Usuario(models.Model):
      id_usuario = models.AutoField(primary_key=True)
      nome = models.CharField(max_length=80)
      datanasc = models.DateField()
      email = models.CharField(max_length=255)
      senha = models.CharField(max_length=255)
      hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,db_column="id_hotel",null=False)
      perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,db_column="id_perfil")
 
      class Meta:
            db_table = 'usuario'
