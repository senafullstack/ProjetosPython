from django.db import models
class Teste(models.Model):
    id_teste = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    class Meta:
        db_table = 'teste'