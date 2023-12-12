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

@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioIndexView(TemplateView):
    template_name = 'admin/usuario/index.html'
    def get(self, request, *args, **kwargs):
        lista = Usuario.objects.all()
        content = {
            "lista": lista
        }
        return render(request,self.template_name,content)  

@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioSalvarView(TemplateView):
    template_name ="admin/usuario/cadastro"
    def post(self, request):
        usuariodao = Usuario()
        usuariodao.nome = request.POST.get('nome')
        usuariodao.email = request.POST.get('email')
        perfil = Perfil.objects.get(id_perfil=request.POST.get('id_perfil'))
        usuariodao.perfil = perfil
        departamento = Departamento.objects.get(id_departamento=request.POST.get('id_departamento'))
        usuariodao.departamento = departamento
        senha = request.POST.get('senha').encode('utf-8')
        senhacriptografadabytes = bcrypt.hashpw(senha,bcrypt.gensalt())
        usuariodao.senha = senhacriptografadabytes.decode('utf-8')
        usuariodao.save()
        print(request.POST.get('id_perfil'))
        return redirect('/admin/usuario')
    
            
@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioCadastroView(TemplateView):
    template_name = 'admin/usuario/cadastro.html'
    def get(self, request, *args, **kwargs):
        reg_perfil = Perfil.objects.all()
        reg_departamento = Departamento.objects.all()
        content = {
            "reg_perfil": reg_perfil,
            "reg_departamento": reg_departamento
        }
        return render(request,self.template_name,content)

@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioExcluirView(TemplateView):
    template_name = 'admin/usuario/index.html'
    def get(self, request,codigo):
        usuario = usuario = get_object_or_404(Usuario, id_usuario=codigo)
        usuario.delete()
        return redirect('/admin/usuario')
    
@method_decorator(custom_login_required, name='dispatch')
class AdminUsuarioExcluirTodosView(TemplateView):
    template_name = 'admin/usuario/index.html'
    def post(self, request):
        dados = request.POST.getlist('dadosexcluir')
        print("DADOS PARA EXCLUIR")
        print(dados)
        for codigo in dados:
            usuario = get_object_or_404(Usuario, id_usuario=codigo)
            usuario.delete()
        return redirect('/admin/usuario')    

@method_decorator(custom_login_required,name='dispatch')
class AdminUsuarioEditarView(TemplateView):
    template_name = 'admin/usuario/editar.html'
    def get(self, request,codigo):
        usuario = Usuario.objects.get(id_usuario=codigo)
        reg_perfil = Perfil.objects.all()
        reg_departamento = Departamento.objects.all()
        content = {
            "reg_perfil": reg_perfil,
            "reg_departamento": reg_departamento,
            "dados":usuario
        }
        return render(request, self.template_name,content)
    
@method_decorator(custom_login_required,name="dispatch")
class AdminUsuarioAtualizarView(TemplateView):
    template_name ="admin/usuario/cadastro"
    def post(self, request):
        id_usuario = request.POST.get("id_usuario")
        usuariodao = Usuario.objects.get(id_usuario=id_usuario)
        usuariodao.nome = request.POST.get('nome')
        usuariodao.email = request.POST.get('email')
        perfil = Perfil.objects.get(id_perfil=request.POST.get('id_perfil'))
        usuariodao.perfil = perfil
        departamento = Departamento.objects.get(id_departamento=request.POST.get('id_departamento'))
        usuariodao.departamento = departamento
        senha = request.POST.get('senha').encode('utf-8')
        senhacriptografadabytes = bcrypt.hashpw(senha,bcrypt.gensalt())
        usuariodao.senha = senhacriptografadabytes.decode('utf-8')
        usuariodao.save()
        print(request.POST.get('id_perfil'))
        return redirect('/admin/usuario')
    
@method_decorator(custom_login_required,name='dispatch')
class AdminUsuarioVisualizarView(TemplateView):
    template_name = 'admin/usuario/visualizar.html'
    def get(self, request,codigo):
        usuario = Usuario.objects.get(id_usuario=codigo)
        content = {
            "dados":usuario
        }
        return render(request, self.template_name,content)     
  
  