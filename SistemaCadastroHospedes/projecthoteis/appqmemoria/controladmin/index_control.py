import requests
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ..models import *
from rest_framework.views import APIView
from ..decorators import custom_login_required
from django.utils.decorators import method_decorator
@method_decorator(custom_login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'admin/home/index.html'
    def get(self, request):
         return render(request,self.template_name)
    
