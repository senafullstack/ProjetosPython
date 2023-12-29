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
class AdminHospedeIndexView(TemplateView):
         template_name = "admin/hospede/index.html"
         def get(self, request, *args, **kwargs):
             lista = Hospede.objects.all()
             content = {
                 "lista": lista
             }
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminHospedeSalvarView(TemplateView):
     template_name ="admin/hospede/cadastro.html"
     def post(self, request):
             tabeladao = Hospede()

             tabeladao.nome = request.POST.get('nome')
             foto= request.FILES.get("foto")
             tabeladao.foto = Arquivos.salvar_imagem(foto,"imagens")
             tabeladao.fone = request.POST.get('fone')
             tabeladao.email = request.POST.get('email')
             tabeladao.cpf = request.POST.get('cpf')
             if request.POST.get("datanasc"):
               datanascoriginal = ValidadorUtil.converter_para_data(request.POST.get("datanasc"))
               if datanascoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if datanascoriginal:
                  tabeladao.datanasc = datanascoriginal.strftime("%Y-%m-%d")
             tabeladao.pai = request.POST.get('pai')
             tabeladao.mae = request.POST.get('mae')
             tabeladao.quarto = request.POST.get('quarto')
             if request.POST.get("entrada"):
               entradaoriginal = ValidadorUtil.converter_para_data(request.POST.get("entrada"))
               if entradaoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if entradaoriginal:
                  tabeladao.entrada = entradaoriginal.strftime("%Y-%m-%d")
             if request.POST.get("saida"):
               saidaoriginal = ValidadorUtil.converter_para_data(request.POST.get("saida"))
               if saidaoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if saidaoriginal:
                  tabeladao.saida = saidaoriginal.strftime("%Y-%m-%d")
             tabeladao.placa = request.POST.get('placa')
             tabeladao.marca = request.POST.get('marca')
             tabeladao.modelo = request.POST.get('modelo')
             tabeladao.cor = request.POST.get('cor')
             id_hotel = request.POST.get("id_hotel")
             if id_hotel is not None and id_hotel != "":
                hotel = Hotel.objects.get(id_hotel=request.POST.get("id_hotel"))
                tabeladao.hotel = hotel
 
             if messages.get_messages(request):
                 return render(request,self.template_name, {"messages": messages.get_messages(request)})
             tabeladao.save()
             return redirect('hospede_index')
@method_decorator(custom_login_required, name="dispatch")
class AdminHospedeCadastroView(TemplateView):
     template_name ="admin/hospede/cadastro.html"
     def get(self, request, *args, **kwargs):
             dados = ""
             reg_hotel = Hotel.objects.all()
             content = {
                  "dados":dados,
                  "reg_hotel": reg_hotel,
             }
 
             return render(request,self.template_name,content)
@method_decorator(custom_login_required, name="dispatch")
class AdminHospedeExcluirView(TemplateView):
         template_name = "admin/hospede/index.html"
         def get(self, request,codigo):
                 dados = get_object_or_404(Hospede, id_hospede=codigo)
                 dados.delete()
                 return redirect('hospede_index')
@method_decorator(custom_login_required, name="dispatch")
class AdminHospedeExcluirTodosView(TemplateView):
         template_name = "admin/hospede/index.html"
         def post(self, request):
             dados = request.POST.getlist("dadosexcluir")
             for codigo in dados:
                     hospede = get_object_or_404(Hospede, id_hospede=codigo)
                     hospede.delete()
             return redirect('hospede_index')  
@method_decorator(custom_login_required,name="dispatch")
class AdminHospedeEditarView(TemplateView):
     template_name = "admin/hospede/editar.html"
     def get(self, request,codigo):
             dados = Hospede.objects.get(id_hospede=codigo)
             reg_hotel = Hotel.objects.all()
             content = {
                  "dados":dados,
                  "reg_hotel": reg_hotel,
             }
 
             return render(request, self.template_name,content)
@method_decorator(custom_login_required,name="dispatch")
class AdminHospedeAtualizarView(TemplateView):
     template_name ="admin/hospede/cadastro.html"
     def post(self, request):
             codigo = request.POST.get("id_hospede")
             tabeladao = Hospede.objects.get(id_hospede=codigo)
             tabeladao.nome = request.POST.get('nome')
             if request.FILES.get("foto"):
               foto= request.FILES.get("foto")
               tabeladao.foto = Arquivos.salvar_imagem(foto,"imagens")
             tabeladao.fone = request.POST.get('fone')
             tabeladao.email = request.POST.get('email')
             tabeladao.cpf = request.POST.get('cpf')
             datanascoriginal = ValidadorUtil.converter_para_data(request.POST.get("datanasc"))
             if request.POST.get("datanasc"):
               datanascoriginal = ValidadorUtil.converter_para_data(request.POST.get("datanasc"))
               if datanascoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if datanascoriginal:
                  tabeladao.datanasc = datanascoriginal.strftime("%Y-%m-%d")
             tabeladao.pai = request.POST.get('pai')
             tabeladao.mae = request.POST.get('mae')
             tabeladao.quarto = request.POST.get('quarto')
             if request.POST.get("entrada"):
               entradaoriginal = ValidadorUtil.converter_para_data(request.POST.get("entrada"))
               if entradaoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if entradaoriginal:
                  tabeladao.entrada = entradaoriginal.strftime("%Y-%m-%d")
             if request.POST.get("saida"):
               saidaoriginal = ValidadorUtil.converter_para_data(request.POST.get("saida"))
               if saidaoriginal is None:
                  messages.error(request, "Campo Data Inválido")
               if saidaoriginal:
                  tabeladao.saida = saidaoriginal.strftime("%Y-%m-%d")
             tabeladao.placa = request.POST.get('placa')
             tabeladao.marca = request.POST.get('marca')
             tabeladao.modelo = request.POST.get('modelo')
             tabeladao.cor = request.POST.get('cor')
             id_hotel = request.POST.get("id_hotel")
             if id_hotel is not None and id_hotel != "":
                hotel = Hotel.objects.get(id_hotel=request.POST.get("id_hotel"))
                tabeladao.hotel = hotel
 
             if messages.get_messages(request):
                 return render(request,self.template_name, {"messages": messages.get_messages(request)})
             tabeladao.save()
             return redirect('hospede_index')
@method_decorator(custom_login_required,name="dispatch")
class AdminHospedeVisualizarView(TemplateView):
            template_name = "admin/hospede/visualizar.html"
            def get(self, request,codigo):
                 dados = Hospede.objects.get(id_hospede=codigo)
                 content = {
                             "dados":dados
                 }
                 return render(request, self.template_name,content)

