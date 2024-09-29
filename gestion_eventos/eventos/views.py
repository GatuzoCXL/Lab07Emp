from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, RegistroEvento
from .forms import EventoForm, RegistroEventoForm

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user  # Asigna el usuario actual como organizador
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def registrar_en_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.evento = evento
            registro.usuario = request.user
            registro.save()
            return redirect('lista_eventos')
    else:
        form = RegistroEventoForm()
    return render(request, 'eventos/registrar_en_evento.html', {'form': form, 'evento': evento})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})
# Create your views here.
