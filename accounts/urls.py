from django.urls import path

from . import views


urlpatterns = [
	path('signup/', views.SignUp.as_view(template_name='signup.html'), name='signup.html'),
	path('usuarios/', views.usuariosRender, name='usuarios.html'),
	path('remover/<int:id>', views.deletarUsuario, name='remover.html'),
]