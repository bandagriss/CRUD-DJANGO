from django import forms

from apps.adopcion.models import Persona

class PersonaForm(forms.ModelForm):

	class Meta:
		model=Persona

		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]

		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'edad': 'Edad',
			'telefono': 'Telefono',
			'email': 'Correo',
			'domicilio': 'Domicilio',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={"class":"form-control"}),
			'apellidos' : forms.TextInput(attrs={"class":"form-control"}),
			'edad' : forms.TextInput(attrs={"class":"form-control"}),
			'telefono' : forms.TextInput(attrs={"class":"form-control"}),
			'email' : forms.TextInput(attrs={"class":"form-control"}),
			'domicilio' : forms.TextInput(attrs={"class":"form-control"}),
		}