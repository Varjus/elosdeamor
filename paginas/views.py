from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class PaginaHome(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'paginas/home.html'    

    