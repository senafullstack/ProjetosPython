from django.db import models
class Departamento(models.Model):
     id_departamento = models.AutoField(primary_key=True)
     descricao = models.CharField(max_length=80)
     class Meta:
         db_table = 'departamento'