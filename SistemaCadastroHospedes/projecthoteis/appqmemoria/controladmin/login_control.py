from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import bcrypt
from django.contrib import messages
## para listar as rotas
from django.urls import get_resolver
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator
from ..models import *
class AdminLoginView(TemplateView):
    print("login aquie")
    template_name = "admin/login/index.html"
    
class AdminEntrarView(TemplateView):
    template_name = 'admin/login/index.html'
    def post(self,request,*args, **kwargs):
        email = request.POST.get('email')
        senha = request.POST.get('senha').encode('utf-8')
        try:
            dados = Usuario.objects.get(email=email)
            print(dados)
        except Usuario.DoesNotExist:
            messages.error(request,self.template_name)
            return render(request,self.template_name, {'messages': messages.get_messages(request)})
        
        senhabase = dados.senha.encode('utf-8')
        if bcrypt.checkpw(senha, senhabase):
            request.session['nome_usuario'] = dados.nome
            request.session['id_usuario'] = dados.id_usuario
            request.session['id_perfil'] = dados.perfil.id_perfil
            if hasattr(dados, 'hotel') and dados.hotel:
                request.session['id_hotel'] = dados.hotel.id_hotel
            else:
                request.session['id_hotel'] = 0
            request.session['usuario_email'] = dados.email
            ######## VERIFICA AS ROTAS QUE O USUARIO TEM ACESSO POR PERFIL
            permissoes = []
            perfil = Perfil.objects.get(id_perfil=dados.perfil.id_perfil)
            dodosperfil = PerfilFormulario.objects.filter(perfil=perfil,permissao='S')
            if dodosperfil is not None:
                for dado in dodosperfil:
                    permissoes.append(dado.formulario.descricao)
                    #print(dado.formulario.descricao)
            ###### VERIFICA AS ROTAS QUE O USUARIO TEM POR USUARIO
            



            request.session["permissoes"]= permissoes
            #print(request.session["permissoesperfil"])
            #print(dodosperfil)
            print(permissoes)
            return redirect('adminhome')
        else:
            # Adicione uma mensagem de erro se a senha estiver incorreta
            messages.error(request, 'Senha incorreta.')
            return render(request, self.template_name,{'messages': messages.get_messages(request)})
class AdminSairView(TemplateView):
    def get(self, request):
        if 'id_usuario' in request.session:
          del request.session['id_usuario']
          
        return redirect('adminlogin')
     