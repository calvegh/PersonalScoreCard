import time
from django.shortcuts import render
from .forms import Formulario


# Create your views here.

def contact(request):
	saludo={'intro':'hellouuu'}
	return render(request,'salud/contacto.html',saludo)
def index(request):
	hora=time.strftime("%H:%M:%S")
	indicadores={
	'ind1':'Salud',
	'ind2':'Deportes',
	'ind3':'Finanzas',
	'ind4':'Dieta',
	'ind5':'Profesional',
	'ind6':'Social',
	'saludo':'Personal ScoreCard',
	'hora':hora}
	return render(request,'salud/index.html',indicadores)
def welcome(request):
	return render(request,'salud/welcome.html')
def info(request):
	return render(request,'salud/info.html')
	
def registrodatos(request):
	form = Formulario()
	context = {'form':form}
	return render(request, 'salud/registrodatos', context)

def salud(request):
	if request.method =='POST':
		form = Formulario(request.POST)
		if form.is_valid():
			context = {'ans':form.cleaned_data}
			print(form.cleaned_data)
			return render(request,'salud/salud.html/',context)
	else:
		form = Formulario()
	return render(request, 'salud/registrosalud.html', {'form':form},)
