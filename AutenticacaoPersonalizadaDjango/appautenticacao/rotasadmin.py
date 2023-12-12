from .viewsadmin import *
from django.urls import path


urlpatterns = [
    path('home',IndexView.as_view(), name='adminhome'),
   
    path('',IndexView.as_view(),name='adminhome'),
    path('login',AdminLoginView.as_view(),name='adminlogin'),
    path('entrar',AdminEntrarView.as_view(),name='adminentrar'), 
    path('sair',AdminSairView.as_view(),name='adminsair'), 
    ## USUARIOS
    path('usuario',AdminUsuarioIndexView.as_view(),name='usuario_index'),
    path('usuario/index',AdminUsuarioIndexView.as_view(),name='usuario_index'),
    path('usuario/cadastro',AdminUsuarioCadastroView.as_view(),name='usuario_cadastro'),
    path('usuario/salvar',AdminUsuarioSalvarView.as_view(),name='usuario_salvar'),
    path('usuario/editar/<int:codigo>',AdminUsuarioEditarView.as_view(),name='usuario_editar'),
    path('usuario/atualizar',AdminUsuarioAtualizarView.as_view(),name='usuario_atualizar'),
    path('usuario/excluir/<int:codigo>',AdminUsuarioExcluirView.as_view(),name='usuario_excluir'),
    path('usuario/excluirtodos',AdminUsuarioExcluirTodosView.as_view(),name='usuario_excluirtodos'),
    path('usuario/visualizar/<int:codigo>',AdminUsuarioVisualizarView.as_view(),name='usuario_visualizar'),
    
    ## formularios
    path('formulario/gravar',AdminFormularioGravarView.as_view(),name='formulario_salvar'),
    ## permissao perfil
    path('permissaoperfil/<int:codigoperfil>',AdminPermissaoperfil.as_view(),name='permissaoperfil_index'),
    path('permissaoperfil/salvar',AdminPermissaoPerfilSalvar.as_view(),name='permissaoperfil_salvar'),
]