from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Setores
from .forms import SetoresForm
from accounts.models import CustomUser
import pdb
from django.contrib.auth.decorators import login_required

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
			return redirect('setores')
	return render(request, 'setores/novosetor.html', {'form':form})

@login_required
def setor(request, id):
	setores = Setores.objects.get(id=id)
	if request.POST != None:
		form = SetoresForm(request.POST or None, instance=setores)
		if form.is_valid():
			form.save()
			return redirect('setores')
	return render(request, 'setores/setor.html', {'setores':setores}, {'form':form})

