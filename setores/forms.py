from django import forms
from .models import Setores, Prioridades
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset


class SetoresForm(forms.ModelForm):
	descricao = forms.CharField(widget=forms.Textarea, label='Descrição')
	class Meta:
		model = Setores
		fields = ('nome', 'descricao', 'telefone',)
	def __init__(self, *args, **kwargs):
		super(SetoresForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('nome', css_class='form-group col-md-6'),
				Column('telefone', css_class='form-group col-md-6'),
				css_class='form-row'
			),
			'descricao'
		)
		self.helper.add_input(Submit('submit', 'Enviar'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))

class PrioridadesForm(forms.ModelForm):
	class Meta:
		model = Prioridades
		fields = ('nome',)
		
	def __init__(self, *args, **kwargs):
		super(PrioridadesForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Enviar'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
		



