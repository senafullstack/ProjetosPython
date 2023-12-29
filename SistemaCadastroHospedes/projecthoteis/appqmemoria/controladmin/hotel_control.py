from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from ..models import *
import bcrypt
from ..classesutil.util import ValidadorUtil,Arquivos
from django.contrib import messages
from django.urls import get_resolver
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator
@method_decorator(custom_login_required, name="dispatch")
class AdminHotelIndexView(TemplateView):
         template_name = "admin/hotel/index.html"
         def get(self, request, *args, **kwargs):
             lista = Hotel.objects.all()
             content = {
                 "lista": lista
             }
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminHotelSalvarView(TemplateView):
     template_name ="admin/hotel/cadastro.html"
     def post(self, request):
             tabeladao = Hotel()

             tabeladao.nome = request.POST.get('nome')
             tabeladao.nomefantasia = request.POST.get('nomefantasia')
             tabeladao.cnpj = request.POST.get('cnpj')
             tabeladao.endereco = request.POST.get('endereco')
             tabeladao.numero = request.POST.get('numero')
             tabeladao.bairro = request.POST.get('bairro')
             tabeladao.cidade = request.POST.get('cidade')
             tabeladao.estado = request.POST.get('estado')
             tabeladao.responsavel = request.POST.get('responsavel')
             tabeladao.fone = request.POST.get('fone')
             tabeladao.email = request.POST.get('email')
 
             if messages.get_messages(request):
                 return render(request,self.template_name, {"messages": messages.get_messages(request)})
             tabeladao.save()
             return redirect("hotel_index")
@method_decorator(custom_login_required, name="dispatch")
class AdminHotelCadastroView(TemplateView):
     template_name ="admin/hotel/cadastro.html"
     def get(self, request, *args, **kwargs):
             dados = ""
             content = {
                  "dados":dados,
             }
 
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminHotelExcluirView(TemplateView):
         template_name = "admin/hotel/index.html"
         def get(self, request,codigo):
                 dados = get_object_or_404(Hotel, id_hotel=codigo)
                 dados.delete()
                 return redirect("hotel_index")
@method_decorator(custom_login_required, name="dispatch")
class AdminHotelExcluirTodosView(TemplateView):
         template_name = "admin/hotel/index.html"
         def post(self, request):
             dados = request.POST.getlist("dadosexcluir")
             for codigo in dados:
                     hotel = get_object_or_404(Hotel, id_hotel=codigo)
                     hotel.delete()
             return redirect("hotel_index")    
@method_decorator(custom_login_required,name="dispatch")
class AdminHotelEditarView(TemplateView):
     template_name = "admin/hotel/editar.html"
     def get(self, request,codigo):
             dados = Hotel.objects.get(id_hotel=codigo)
             content = {
                  "dados":dados,
             }
 
             return render(request, self.template_name,content)
@method_decorator(custom_login_required,name="dispatch")
class AdminHotelAtualizarView(TemplateView):
     template_name ="admin/hotel/cadastro.html"
     def post(self, request):
             codigo = request.POST.get("id_hotel")
             tabeladao = Hotel.objects.get(id_hotel=codigo)
 
             tabeladao.nome = request.POST.get('nome')
             tabeladao.nomefantasia = request.POST.get('nomefantasia')
             tabeladao.cnpj = request.POST.get('cnpj')
             tabeladao.endereco = request.POST.get('endereco')
             tabeladao.numero = request.POST.get('numero')
             tabeladao.bairro = request.POST.get('bairro')
             tabeladao.cidade = request.POST.get('cidade')
             tabeladao.estado = request.POST.get('estado')
             tabeladao.responsavel = request.POST.get('responsavel')
             tabeladao.fone = request.POST.get('fone')
             tabeladao.email = request.POST.get('email')
 
             if messages.get_messages(request):
                 return render(request,self.template_name, {"messages": messages.get_messages(request)})
             tabeladao.save()
             return redirect("hotel_index")
@method_decorator(custom_login_required,name="dispatch")
class AdminHotelVisualizarView(TemplateView):
            template_name = "admin/hotel/visualizar.html"
            def get(self, request,codigo):
                 dados = Hotel.objects.get(id_hotel=codigo)
                 content = {
                             "dados":dados
                 }
                 return render(request, self.template_name,content)

