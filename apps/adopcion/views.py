from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.adopcion.models import Persona
from apps.adopcion.forms import PersonaForm

# Create your views here.

def index(request):
	personas = Persona.objects.all()
	contexto = {'personas': personas}
	return render(request, 'adopcion/index.html', contexto)

def new(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('persona:index')
	else:
		form = PersonaForm()
	return render(request, 'adopcion/form.html', {'form': form})

def edit(request, id_persona):
	persona = Persona.objects.get(id=id_persona)
	if request.method == 'GET':
		form = PersonaForm(instance=persona)
	else:
		form = PersonaForm(request.POST, instance=persona)
		if form.is_valid():
			form.save()
		return redirect('persona:index')
	return render(request, 'adopcion/form.html', {'form':form})

def destroy(request, id_persona):
	persona = Persona.objects.get(id=id_persona)
	if request.method == 'POST':
		persona.delete()
		return redirect('persona:index')
	return render(request, 'adopcion/destroy.html', {'persona':persona})



