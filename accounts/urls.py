from django.urls import path
from . import views
from setores.models import Setores

setores = {'setores':Setores.objects.all()}

urlpatterns = [
	path('signup/', views.SignUp.as_view(template_name='signup.html'), name='signup.html'),
	path('usuarios/', views.usuariosRender, name='usuarios.html'),
	path('remover/<int:id>', views.deletarUsuario, name='remover.html'),
	path('conta/<int:id>', views.minhaConta, name='conta'),
]