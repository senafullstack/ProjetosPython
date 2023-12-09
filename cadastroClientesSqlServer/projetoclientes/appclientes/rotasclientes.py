from django.urls import path,include
from .views import *
urlpatterns = [
    path('',ClienteIndexView.as_view(),name='cliente_index'),
    path('cadastro',ClienteCadastroView.as_view(),name='cliente_cadastro'),
    path('salvar',ClienteSalvarView.as_view(),name='cliente_salvar'),
    path('editar/<int:codigo>',ClienteEditarView.as_view(),name='cliente_editar'),
    path('atualizar',ClienteAtualizarView.as_view(),name='cliente_atualizar'),
    path('excluir/<int:codigo>',ClienteExcluirView.as_view(),name='cliente_excluir'),  
    path('buscar',ClienteBuscarView.as_view(),name='cliente_buscar'),  
]
