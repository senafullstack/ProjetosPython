from django.shortcuts import render
from django.db.models import Q 
from datetime import datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Clientes
from django.contrib import messages
from django.urls import get_resolver
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .utils import ValidadorUtil
import requests
class ClienteIndexView(ListView):
    template_name = 'cliente/index.html'
    model = Clientes
    context_object_name = 'lista'
    paginate_by = 30
    def get_queryset(self):
        return Clientes.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagina'] = self.request.GET.get('pagina')
        return context
   
    
class ClienteCadastroView(TemplateView):
    template_name = 'cliente/cadastro.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)  
class ClienteSalvarView(TemplateView):
    template_name ="cliente/cadastro.html"
    def post(self, request):
        clientedb = Clientes()
        clientedb.nome = request.POST.get('nome')
        if not request.POST.get('datanasc'):
            messages.error(request, 'Campo Data de nascimento é obrigatório.')
        if not clientedb.nome:
            messages.error(request, 'Campo Nome é obrigatório.')
        dataoriginal = ValidadorUtil.converter_para_data(request.POST.get('datanasc'))
        if dataoriginal is None:
            messages.error(request, 'Campo Data Inválido')
        if dataoriginal:
            ##data_objeto = datetime.strptime(dataoriginal, "%d/%m/%Y")
            clientedb.datanasc = dataoriginal.strftime("%Y-%m-%d")
        if ValidadorUtil.validar_email(request.POST.get('email')):
            clientedb.email = request.POST.get('email')
        else:
            messages.error(request, 'Email Inválido')    
        
        clientedb.cep = request.POST.get('cep')
        clientedb.rua = request.POST.get('rua')
        clientedb.numero = request.POST.get('numero')
        clientedb.estado = request.POST.get('estado')
        clientedb.cidade = request.POST.get('cidade')
        clientedb.bairro = request.POST.get('bairro')
        
        if messages.get_messages(request):
            return render(request,self.template_name, {'messages': messages.get_messages(request)})
        clientedb.save()
        return redirect('cliente_index')
class ClienteEditarView(TemplateView):
    template_name = 'cliente/editar.html'
    def get(self, request,codigo):
        cliente = Clientes.objects.get(id_cliente=codigo)
        content = {
            "dados":cliente
        }
        return render(request, self.template_name,content)    

class ClienteAtualizarView(TemplateView):
    template_name ="cliente/editar.html"
    def post(self, request):
        id_cliente= request.POST.get("id_cliente")
        clientedb = Clientes.objects.get(id_cliente=id_cliente)
        clientedb.nome = request.POST.get('nome')
        if not request.POST.get('datanasc'):
            messages.error(request, 'Campo Data de nascimento é obrigatório.')
        if not clientedb.nome:
            messages.error(request, 'Campo Nome é obrigatório.')
        dataoriginal = ValidadorUtil.converter_para_data(request.POST.get('datanasc'))
        if dataoriginal is None:
            messages.error(request, 'Campo Data Inválido')
        if dataoriginal:
            ##data_objeto = datetime.strptime(dataoriginal, "%d/%m/%Y")
            clientedb.datanasc = dataoriginal.strftime("%Y-%m-%d")
        if ValidadorUtil.validar_email(request.POST.get('email')):
            clientedb.email = request.POST.get('email')
        else:
            messages.error(request, 'Email Inválido')  
        clientedb.cep = request.POST.get('cep')
        clientedb.rua = request.POST.get('rua')
        clientedb.numero = request.POST.get('numero')
        clientedb.estado = request.POST.get('estado')
        clientedb.cidade = request.POST.get('cidade')
        clientedb.bairro = request.POST.get('bairro')
        content = {
            "dados":clientedb,
            'messages': messages.get_messages(request)
        }
        if messages.get_messages(request):
            return render(request,self.template_name, content)
        clientedb.save()
        return redirect('cliente_index')
class ClienteExcluirView(TemplateView):
    template_name = 'cliente/index.html'
    def get(self, request,codigo):
        cliente  = get_object_or_404(Clientes, id_cliente=codigo)
        cliente.delete()
        return redirect('cliente_index') 
    
class ClienteBuscarView(TemplateView):
    template_name ="cliente/index.html"
    def post(self, request):
        filtro = request.POST.get('filtro')
        if filtro:
            lista = Clientes.objects.filter(
                Q(nome__icontains=filtro) | Q(email__icontains=filtro)
            )
        else:
            lista = Clientes.objects.all()
        content = {
            "lista": lista
        }
        return render(request,self.template_name,content)      
    
    
class BuscaCEPView(TemplateView):
    template_name ="cep/index.html"
    def get(self, request):
        content = {
            "lista": ''
        }
        return render(request,self.template_name,content)   
    def post(self, request):
        cep = request.POST.get('cep')
        if(cep):
             api_url = f'https://viacep.com.br/ws/{cep}/json/'
             response = requests.get(api_url)
             if response.status_code == 200:
                data = response.json()
                content = {
                    "lista": data
                }
             else:
                content = {
                    "lista": {'erro': 'Erro ao consultar o CEP'}
                }
        else:
            content = {
                    "lista": {'erro': 'Erro ao consultar o CEP'}
                }
        return render(request,self.template_name,content)      