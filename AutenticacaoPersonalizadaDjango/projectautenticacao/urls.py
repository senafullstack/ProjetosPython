from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', include('appqmemoria.rotasadmin')),
    path('',include('appqmemoria.rotassite'))
   
]
