from django import forms

class Formulario(forms.Form):
	Medita= forms.BooleanField(label='Medite?')