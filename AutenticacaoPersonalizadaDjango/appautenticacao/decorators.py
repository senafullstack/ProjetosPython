from functools import wraps
from django.shortcuts import redirect
from django.urls import resolve

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verificar se as informações de usuário estão na sessão
        id_usuario = request.session.get('id_usuario')
        id_perfil = request.session.get('id_perfil')
        nome_usuario =request.session.get('nome_usuario')
        print(nome_usuario)
        if id_usuario is None:
            # Se não estiver, redirecionar para a página de login
            return redirect('adminlogin')
        ## aqui criar outras acoes 
        nomerota = resolve(request.path_info).url_name
        print(nomerota)
        print(id_perfil)
        
        print(request.session.get('permissoes'))
        if(nomerota in request.session.get('permissoes')):
            print("TEM PERFMISSAO AQUI")
        # Se as informações estiverem na sessão, chamar a view original
        return view_func(request, *args, **kwargs)
    return _wrapped_view
