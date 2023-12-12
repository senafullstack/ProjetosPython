from django.shortcuts import render, redirect
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
class AdminPermissaoperfil(TemplateView):
    template_name = 'admin/permissaoperfil/index.html'
    def get(self, request,codigoperfil, *args, **kwargs):
        perfilformulariodb = PerfilFormulario.objects.filter(perfil_id=codigoperfil)
        context = {
            'listapf':perfilformulariodb,
            "codigoperfil":codigoperfil
        }
        return render(request, self.template_name,context)
class AdminFormularioGravarView(TemplateView):
    template_name = 'admin/home/index.html'
    def get(self, request):
        resolver = get_resolver()
        perfildao = Perfil.objects.all()
        nome_rotas = [nome_rota for nome_rota in resolver.reverse_dict]
        for nome_rota in nome_rotas:
            if callable(nome_rota) and 'View' in str(nome_rota):
                continue
            print(f'Nome da Rota: {nome_rota}')
            formulariodao = Formulario()
            total = Formulario.objects.filter(descricao=nome_rota).count()
            #print(total)
            if(total==0):
                formulariodao.descricao = nome_rota
                formulariodao.save()
                for perfil in perfildao:
                    perfil = Perfil.objects.get(id_perfil=perfil.id_perfil)
                    formulario = Formulario.objects.get(id_formulario=formulariodao.id_formulario)
                    perfilformulariodao = PerfilFormulario()
                    perfilformulariodao.perfil = perfil
                    perfilformulariodao.formulario = formulario
                    perfilformulariodao.permissao = 'S'
                    perfilformulariodao.save();                
        # Crie uma resposta HTTP para exibir as rotas
        #print(resposta)
        content = {
            'rotas':'resposta'
        }
        return render(request,'admin/home/index.html',content)

class AdminPermissaoPerfilSalvar(TemplateView):
       template_name = 'admin/permissaoperfil/index.html'
       def post(self, request):
           codigoperfil = request.POST.get('codigoperfil')
           PerfilFormulario.objects.filter(perfil_id=codigoperfil).update(permissao='N')
           permissoes = request.POST.getlist('permissoes')
           for permisso in permissoes:
               #print(permisso)
               perfilformulariodb = PerfilFormulario.objects.filter(id_perfilformulario=permisso).update(permissao='S')
               
           return redirect('/admin/permissaoperfil/'+codigoperfil)  