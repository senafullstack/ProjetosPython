from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ..models import *
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator
class IndexView(TemplateView):
    template_name = 'home/index.html'