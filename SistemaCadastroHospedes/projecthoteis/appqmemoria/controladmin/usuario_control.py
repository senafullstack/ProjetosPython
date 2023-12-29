from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from ..models import *
import bcrypt
from django.contrib import messages
## para listar as rotas
from django.urls import get_resolver
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator

#@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioIndexView(TemplateView):
    template_name = "admin/usuario/index.html"
    def get(self, request, *args, **kwargs):
        lista = Usuario.objects.all()
        content = {
            "lista": lista
        }
        return render(request,self.template_name,content)  

#@method_decorator(custom_login_required, name="dispatch")
class AdminUsuarioSalvarView(TemplateView):
    template_name ="admin/usuario/cadastro"
    def post(self, request):
        tabeladao = Usuario()
        tabeladao.nome = request.POST.get('nome')
        tabeladao.email = request.POST.get('email')
        perfil = Perfil.objects.get(id_perfil=request.POST.get('id_perfil'))
        tabeladao.perfil = perfil
        if request.POST.get('id_hotel'):
            hotel = Hotel.objects.get(id_hotel=request.POST.get('id_hotel'))
            tabeladao.hotel = hotel
        senha = request.POST.get('senha').encode('utf-8')
        senhacriptografadabytes = bcrypt.hashpw(senha,bcrypt.gensalt())
        tabeladao.senha = senhacriptografadabytes.decode('utf-8')
        tabeladao.save()
        return redirect('usuario_index')
    
            
#@method_decorator(custom_login_required, name="dispatch")
class AdminUsuarioCadastroView(TemplateView):
    template_name = 'admin/usuario/cadastro.html'
    def get(self, request, *args, **kwargs):
        reg_perfil = Perfil.objects.all()
        reg_hotel = Hotel.objects.all()
        content = {
            "reg_perfil": reg_perfil,
            "reg_hotel": reg_hotel
        }
        return render(request,self.template_name,content)

#@method_decorator(custom_login_required, name="dispatch")
class AdminUsuarioExcluirView(TemplateView):
    template_name = "admin/usuario/index.html"
    def get(self, request,codigo):
        dados = get_object_or_404(Usuario, id_usuario=codigo)
        dados.delete()
        return redirect('usuario_index')
    
@method_decorator(custom_login_required, name="dispatch")
class AdminUsuarioExcluirTodosView(TemplateView):
    template_name = "admin/usuario/index.html"
    def post(self, request):
        dados = request.POST.getlist("dadosexcluir")
        for codigo in dados:
            usuario = get_object_or_404(Usuario, id_usuario=codigo)
            usuario.delete()
        return redirect('usuario_index')   

@method_decorator(custom_login_required,name="dispatch")
class AdminUsuarioEditarView(TemplateView):
    template_name = "admin/usuario/editar.html"
    def get(self, request,codigo):
        dados = Usuario.objects.get(id_usuario=codigo)
        reg_perfil = Perfil.objects.all()
        reg_hotel = Hotel.objects.all()
        content = {
            "reg_perfil": reg_perfil,
            "reg_hotel": reg_hotel,
            "dados":dados
        }
        return render(request, self.template_name,content)
    
@method_decorator(custom_login_required,name="dispatch")
class AdminUsuarioAtualizarView(TemplateView):
    template_name ="admin/usuario/cadastro"
    def post(self, request):
        codigo = request.POST.get("id_usuario")
        tabeladao = Usuario.objects.get(id_usuario=codigo)
        tabeladao.nome = request.POST.get('nome')
        tabeladao.email = request.POST.get('email')
        if 'id_perfil' in request.POST and request.POST['id_perfil'].isdigit():
            perfil = Perfil.objects.get(id_perfil=request.POST.get('id_perfil'))
            tabeladao.perfil = perfil
        if 'id_hotel' in request.POST and request.POST['id_hotel'].isdigit():
            hotel = Hotel.objects.get(id_hotel=request.POST.get('id_hotel'))
            tabeladao.hotel = hotel
        if request.POST.get('senha'):    
            senha = request.POST.get('senha').encode('utf-8')
            senhacriptografadabytes = bcrypt.hashpw(senha,bcrypt.gensalt())
            tabeladao.senha = senhacriptografadabytes.decode('utf-8')
        tabeladao.save()
        return redirect('usuario_index')
    
@method_decorator(custom_login_required,name="dispatch")
class AdminUsuarioVisualizarView(TemplateView):
    template_name = "admin/usuario/visualizar.html"
    def get(self, request,codigo):
        usuario = Usuario.objects.get(id_usuario=codigo)
        content = {
            "dados":usuario
        }
        return render(request, self.template_name,content)     
  
  