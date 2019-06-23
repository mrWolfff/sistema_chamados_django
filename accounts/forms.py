from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset 

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email', 'setor', 'imagem')

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Criar'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class="btn-danger"))

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'setor', 'imagem')

