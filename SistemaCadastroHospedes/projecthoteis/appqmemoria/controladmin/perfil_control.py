from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from ..models import *
import bcrypt
from django.contrib import messages
from django.urls import get_resolver
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator
@method_decorator(custom_login_required, name="dispatch")
class AdminPerfilIndexView(TemplateView):
         template_name = "admin/perfil/index.html"
         def get(self, request, *args, **kwargs):
             lista = Perfil.objects.all()
             content = {
                 "lista": lista
             }
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminPerfilSalvarView(TemplateView):
     template_name ="admin/perfil/cadastro.html"
     def post(self, request):
             tabeladao = Perfil()

             tabeladao.descricao = request.POST.get('descricao')
 
             tabeladao.save()
             return redirect("perfil_index")
@method_decorator(custom_login_required, name="dispatch")
class AdminPerfilCadastroView(TemplateView):
     template_name ="admin/perfil/cadastro.html"
     def get(self, request, *args, **kwargs):
             content = {
                 "lista": ""
             }
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminPerfilExcluirView(TemplateView):
         template_name = "admin/perfil/index.html"
         def get(self, request,codigo):
                 dados = get_object_or_404(Perfil, id_perfil=codigo)
                 dados.delete()
                 return redirect("perfil_index")
@method_decorator(custom_login_required, name="dispatch")
class AdminPerfilExcluirTodosView(TemplateView):
         template_name = "admin/perfil/index.html"
         def post(self, request):
             dados = request.POST.getlist("dadosexcluir")
             for codigo in dados:
                     perfil = get_object_or_404(Perfil, id_perfil=codigo)
                     perfil.delete()
             return redirect("perfil_index")  
@method_decorator(custom_login_required,name="dispatch")
class AdminPerfilEditarView(TemplateView):
     template_name = "admin/perfil/editar.html"
     def get(self, request,codigo):
             dados = Perfil.objects.get(id_perfil=codigo)
             content = {
                      "dados":dados
             }
             return render(request, self.template_name,content)
@method_decorator(custom_login_required,name="dispatch")
class AdminPerfilAtualizarView(TemplateView):
     template_name ="admin/perfil/cadastro.html"
     def post(self, request):
             codigo = request.POST.get("id_perfil")
             tabeladao = Perfil.objects.get(id_perfil=codigo)
 
             tabeladao.descricao = request.POST.get('descricao')
 
             tabeladao.save()
             return redirect("perfil_index")
@method_decorator(custom_login_required,name="dispatch")
class AdminPerfilVisualizarView(TemplateView):
            template_name = "admin/perfil/visualizar.html"
            def get(self, request,codigo):
                 dados = Perfil.objects.get(id_perfil=codigo)
                 content = {
                             "dados":dados
                 }
                 return render(request, self.template_name,content)

