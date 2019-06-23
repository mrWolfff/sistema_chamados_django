from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
import pdb
from django.views.generic import CreateView
from .models import Chamados
from .forms import ChamadosForm
from setores.models import Setores
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from .forms import ContatoForm
from accounts.models import CustomUser


def baseRender(request):
	return render(request, 'sistemaChamado/base.html')

@login_required
def chamadosRender(request):
	form = Chamados.objects.all()
	setores = Setores.objects.all()
	usuarios = CustomUser.objects.all()	
	if request.POST != None:
		form = ChamadosForm(request.POST)	
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'sistemaChamado/chamados.html', {'form':form, 'setores':setores, 'usuarios':usuarios})

@login_required
def index(request):
	cont = 	Chamados.objects.count()
	chamados = Chamados.objects.all()
	cont_concluidos = chamados.filter(status__icontains='Concluído').count()
	cont_abertos = chamados.filter(status__icontains='Não Realizado').count()
	cont_andamento = chamados.filter(status__icontains='Em Andamento').count()
	contador = cont(chamados)
	context = {
		'chamados':chamados,
		'cont':cont,
		'cont_concluidos':cont_concluidos,
		'cont_abertos':cont_abertos,
		'cont_andamento':cont_andamento,
		'contador':contador
	}
	return render(request, 'sistemaChamado/index.html', context)

@login_required
def indexAbertos(request):
	chamados = Chamados.objects.all()
	cont = 	Chamados.objects.count()
	chamados =  chamados.filter(status__icontains='Não Realizado')
	cont_concluidos = chamados.filter(status__icontains='Concluído').count()
	cont_abertos = chamados.filter(status__icontains='Não Realizado').count()
	context = {
		'chamados':chamados,
		'cont':cont,
		'cont_concluidos':cont_concluidos,
		'cont_abertos':cont_abertos,
		'cont_andamento':cont_andamento
	}
	return render(request, 'sistemaChamado/abertos.html', context)

@login_required
def indexConcluidos(request):
	chamados = Chamados.objects.all()
	cont = 	Chamados.objects.count()
	chamados =  chamados.filter(status__icontains='Concluído')
	cont_concluidos = chamados.filter(status__icontains='Concluído').count()
	cont_abertos = chamados.filter(status__icontains='Não Realizado').count()
	context = {
		'chamados':chamados,
		'cont':cont,
		'cont_concluidos':cont_concluidos,
		'cont_abertos':cont_abertos,
	}
	return render(request, 'sistemaChamado/concluidos.html', context)


@login_required
def atualizar(request, id):
	chamados = Chamados.objects.get(id=id)
	if request.POST != None:
		form = ChamadosForm(request.POST or None, instance=chamados)
		if form.is_valid():
			form.save()
			return redirect('index')	
	return render(request, 'sistemaChamado/atualizar.html', {'chamados': chamados})

@login_required
def deletarChamado(request, id):
	chamado = Chamados.objects.get(id=id)

	if request.POST != None:
		chamado.delete()
		return redirect('index.html')
	return render(request, 'sistemaChamado/deletar.html', {'chamado': chamado})


#Contato
def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']

            try:
                send_mail(assunto, msg, emissor, ['lucasewolflew@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('obg')
    return render(request, 'sistemaChamado/contato.html', {'form': email_form})

def obg(request):
    return HttpResponse("<h2>Obrigado pela mensagem!!!</h2>")
