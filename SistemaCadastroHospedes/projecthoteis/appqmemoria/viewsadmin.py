from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
import bcrypt
from django.contrib import messages
## para listar as rotas
from django.urls import get_resolver
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .decorators import custom_login_required
from django.utils.decorators import method_decorator
from .controladmin.index_control import *
from .controladmin.login_control import *
from .controladmin.usuario_control import *
from .controladmin.perfilformulario_control import *

from .controladmin.perfil_control import *



from .controladmin.hotel_control import *

from .controladmin.hospede_control import *
