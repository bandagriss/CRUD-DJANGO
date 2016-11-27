from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm, VacunaForm
from apps.mascota.models import Mascota, Vacuna
# Create your views here.

def index(request):
	return render(request, 'mascota/index.html')


def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
	mascotas = Mascota.objects.all().order_by('id')
	contexto = {'mascotas': mascotas}
	return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

#vacuna no deberia ir aqui sino en otro app pero por el mmomento xD
def vacuna_list(request):
	vacunas = Vacuna.objects.all().order_by('id')
	contexto = {'vacunas': vacunas}
	return render(request, 'mascota/vacuna_list.html', contexto)

def vacuna_create(request):
	if request.method == 'POST':
		form = VacunaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:vacuna_listar')
	else:
		form = VacunaForm()
	return render(request, 'mascota/vacuna_form.html', {'form': form})

def vacuna_edit(request, id_vacuna):
	vacuna = Vacuna.objects.get(id=id_vacuna)
	if request.method == 'GET':
		form = VacunaForm(instance=vacuna)
	else:
		form = VacunaForm(request.POST, instance=vacuna)
		if form.is_valid():
			form.save()
		return redirect('mascota:vacuna_listar')
	return render(request, 'mascota/vacuna_form.html', {'form': form})

def vacuna_delete(request, id_vacuna):
	vacuna = Vacuna.objects.get(id=id_vacuna)
	if request.method == 'POST':
		vacuna.delete()
		return redirect('mascota:vacuna_listar')
	return render(request, 'mascota/vacuna_delete.html', {'vacuna':vacuna})