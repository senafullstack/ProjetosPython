from django.db import models
from .formulariodb import Formulario
from .perfildb import Perfil
class PerfilFormulario(models.Model):
    id_perfilformulario = models.AutoField(primary_key=True)
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,db_column='id_perfil',null=True)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE,db_column='id_formulario',null=True)
    permissao = models.CharField(max_length=1,default='N') 
    class Meta:
        db_table ='perfilformulario'