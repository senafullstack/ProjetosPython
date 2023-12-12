from django.db import models
class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    class Meta:
        db_table = 'perfil'

