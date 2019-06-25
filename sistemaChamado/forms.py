from django import forms
from .models import Chamados,Prioridades
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset


class ChamadosForm(forms.ModelForm):
	class Meta:
		model = Chamados
		fields = ('assunto', 'descricao', 'status', 'usuario', 'solucao')

class ChamadosChangeForm(forms.ModelForm):
	class Meta:

		model = Chamados
		fields = ('assunto', 'descricao', 'prioridade', 'setor')

	def __init__(self, *args, **kwargs):
		super(ChamadosChangeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Enviar'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))

class ContatoForm(forms.Form):
	emissor = forms.EmailField(required=True, label='Remetente')
	assunto = forms.CharField(required=True)
	msg = forms.CharField(widget=forms.Textarea, label='Mensagem')


	def __init__(self, *args, **kwargs):
		super(ContatoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
			Column('emissor', css_class='form-group col-md-6'),
			Column('assunto', css_class='form-group col-md-6'),
			css_class='form-row'
			),
			'msg'
		)
		self.helper.add_input(Submit('submit', 'Enviar'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))





