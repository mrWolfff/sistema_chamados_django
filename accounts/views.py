from django.urls import reverse_lazy
from django.views import generic
from . forms import CustomUserCreationForm
from . models import CustomUser
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
import pdb


def usuariosRender(request):
	usuarios = CustomUser.objects.all()
	return render(request, 'sistemaChamado/usuarios.html', {'usuarios':usuarios})

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('index.html')
	template_name = 'signup.html'

def deletarUsuario(request, id):
	usuario = CustomUser.objects.get(id=id)
	if request.POST != None:
		usuario.delete()
		return redirect('usuarios.html')
	return render(request, 'sistemaChamado/remover.html', {'usuario': usuario})