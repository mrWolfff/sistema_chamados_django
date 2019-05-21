from django import forms
from .models import Chamados, Usuarios


class ChamadosForm(forms.ModelForm):
	class Meta:
		model = Chamados
		fields = ('assunto', 'descricao', 'prioridade', 'status', 'usuario', 'solucao')


