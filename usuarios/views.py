from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class UsuarioCreate(CreateView):
    template_name = 'usuarios/form.html'
    model = User
    fields = ['username', 'email', 'password']

    
