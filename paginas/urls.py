from django.urls import path
from .views import PaginaInicial, PaginaHome

urlpatterns = [

    path('', PaginaInicial.as_view(), name='abrigo'),
    path('inicio/', PaginaHome.as_view(), name='inicio'),

]
