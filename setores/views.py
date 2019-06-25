from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Setores, Prioridades
from .forms import SetoresForm, PrioridadesForm
from accounts.models import CustomUser
import pdb
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def setores(request):
	setores = Setores.objects.all()
	usuarios = CustomUser.objects.all()
	return render(request, 'setores/setores.html', {'setores':setores}, {'usuarios': usuarios})

@login_required
def novoSetor(request):
	form = Setores.objects.all()
	if request.POST != None:
		form = SetoresForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Setor Cadastrado!', extra_tags='alert')
			return redirect('setores')
	return render(request, 'setores/novosetor.html', {'form':form})

@login_required
def setor(request, id):
	setores = Setores.objects.get(id=id)
	if request.POST != None:
		form = SetoresForm(request.POST or None, instance=setores)
		if form.is_valid():
			form.save()
			messages.success(request, 'Setor Alterado!', extra_tags='alert')
			return redirect('setores')
	return render(request, 'setores/setor.html', {'setores':setores}, {'form':form})

@login_required
def prioridades(request):
	form = Prioridades.objects.all()	
	if request.POST != None:
		form = PrioridadesForm(request.POST)	
		if form.is_valid():
			form.save()
			messages.success(request, 'Prioridade Cadastrada!', extra_tags='alert')
			return redirect('index')
	return render(request, 'sistemaChamado/prioridades.html', {'form':form})