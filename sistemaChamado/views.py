from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
import pdb
from django.views.generic import CreateView
from .models import Chamados
from .forms import ChamadosForm

def baseRender(request):
	return render(request, 'sistemaChamado/base.html')

def chamadosRender(request):
	form = Chamados.objects.all()
	
	if request.POST != None:
		form = ChamadosForm(request.POST)	
		if form.is_valid():
			form.save()
			return redirect('index.html')
	return render(request, 'sistemaChamado/chamados.html', {'form':form})

def index(request):
	chamados = Chamados.objects.all()
	return render(request, 'sistemaChamado/index.html', {'chamados':chamados})

def atualizar(request, id):
	chamados = Chamados.objects.get(id=id)
	if request.POST != None:
		form = ChamadosForm(request.POST or None, instance=chamados)
		if form.is_valid():
			form.save()
			return redirect('index.html')
	return render(request, 'sistemaChamado/atualizar.html', {'chamados': chamados})

def deletarChamado(request, id):
	chamado = Chamados.objects.get(id=id)

	if request.POST != None:
		chamado.delete()
		return redirect('index.html')
	return render(request, 'sistemaChamado/deletar.html', {'chamado': chamado})

def filtrar(request):
	chamados = Chamados.objects.all()
	if request.GET.get("filtro") != 'Nenhum':
		filtro = request.GET.get("filtro")
		chamados =  chamados.filter(status__icontains=filtro)
	return render(request, 'sistemaChamado/index.html', {'chamados': chamados})

