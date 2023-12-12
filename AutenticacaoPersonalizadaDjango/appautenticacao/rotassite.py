from django.urls import path
from .controlsite.index_control import *

urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('home',IndexView.as_view(),name='home'),
    
]