from django.db import models
class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    class Meta:
        db_table = 'formulario'