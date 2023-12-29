from .viewsadmin import *
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('home',IndexView.as_view(), name='adminhome'),
   
    path('',IndexView.as_view(),name='adminhome'),
    path('login',AdminLoginView.as_view(),name='adminlogin'),
    path('entrar',AdminEntrarView.as_view(),name='adminentrar'), 
    path('sair',AdminSairView.as_view(),name='adminsair'), 
    ## USUARIOS
    path("usuario",AdminUsuarioIndexView.as_view(),name="usuario_index"),
    path("usuario/index",AdminUsuarioIndexView.as_view(),name="usuario_index"),
    path("usuario/cadastro",AdminUsuarioCadastroView.as_view(),name="usuario_cadastro"),
    path("usuario/salvar",AdminUsuarioSalvarView.as_view(),name="usuario_salvar"),
    path("usuario/editar/<int:codigo>",AdminUsuarioEditarView.as_view(),name="usuario_editar"),
    path("usuario/atualizar",AdminUsuarioAtualizarView.as_view(),name="usuario_atualizar"),
    path("usuario/excluir/<int:codigo>",AdminUsuarioExcluirView.as_view(),name="usuario_excluir"),
    path("usuario/excluirtodos",AdminUsuarioExcluirTodosView.as_view(),name="usuario_excluirtodos"),
    path("usuario/visualizar/<int:codigo>",AdminUsuarioVisualizarView.as_view(),name="usuario_visualizar"),
    
    ## formularios
    path('formulario/gravar',AdminFormularioGravarView.as_view(),name='formulario_salvar'),
    ## permissao perfil
    path('permissaoperfil/<int:codigoperfil>',AdminPermissaoperfil.as_view(),name='permissaoperfil_index'),
    path('permissaoperfil/salvar',AdminPermissaoPerfilSalvar.as_view(),name='permissaoperfil_salvar'),
  



##Perfil##
    path("perfil",AdminPerfilIndexView.as_view(),name="perfil_index"),
    path("perfil/index",AdminPerfilIndexView.as_view(),name="perfil_index"),
    path("perfil/cadastro",AdminPerfilCadastroView.as_view(),name="perfil_cadastro"),
    path("perfil/salvar",AdminPerfilSalvarView.as_view(),name="perfil_salvar"),
    path("perfil/editar/<int:codigo>",AdminPerfilEditarView.as_view(),name="perfil_editar"),
    path("perfil/atualizar",AdminPerfilAtualizarView.as_view(),name="perfil_atualizar"),
    path("perfil/excluir/<int:codigo>",AdminPerfilExcluirView.as_view(),name="perfil_excluir"),
    path("perfil/excluirtodos",AdminPerfilExcluirTodosView.as_view(),name="perfil_excluirtodos"),
    path("perfil/visualizar/<int:codigo>",AdminPerfilVisualizarView.as_view(),name="perfil_visualizar"),



##Hotel##
    path("hotel",AdminHotelIndexView.as_view(),name="hotel_index"),
    path("hotel/index",AdminHotelIndexView.as_view(),name="hotel_index"),
    path("hotel/cadastro",AdminHotelCadastroView.as_view(),name="hotel_cadastro"),
    path("hotel/salvar",AdminHotelSalvarView.as_view(),name="hotel_salvar"),
    path("hotel/editar/<int:codigo>",AdminHotelEditarView.as_view(),name="hotel_editar"),
    path("hotel/atualizar",AdminHotelAtualizarView.as_view(),name="hotel_atualizar"),
    path("hotel/excluir/<int:codigo>",AdminHotelExcluirView.as_view(),name="hotel_excluir"),
    path("hotel/excluirtodos",AdminHotelExcluirTodosView.as_view(),name="hotel_excluirtodos"),
    path("hotel/visualizar/<int:codigo>",AdminHotelVisualizarView.as_view(),name="hotel_visualizar"),


##Hospede##
    path("hospede",AdminHospedeIndexView.as_view(),name="hospede_index"),
    path("hospede/index",AdminHospedeIndexView.as_view(),name="hospede_index"),
    path("hospede/cadastro",AdminHospedeCadastroView.as_view(),name="hospede_cadastro"),
    path("hospede/salvar",AdminHospedeSalvarView.as_view(),name="hospede_salvar"),
    path("hospede/editar/<int:codigo>",AdminHospedeEditarView.as_view(),name="hospede_editar"),
    path("hospede/atualizar",AdminHospedeAtualizarView.as_view(),name="hospede_atualizar"),
    path("hospede/excluir/<int:codigo>",AdminHospedeExcluirView.as_view(),name="hospede_excluir"),
    path("hospede/excluirtodos",AdminHospedeExcluirTodosView.as_view(),name="hospede_excluirtodos"),
    path("hospede/visualizar/<int:codigo>",AdminHospedeVisualizarView.as_view(),name="hospede_visualizar"),
]

