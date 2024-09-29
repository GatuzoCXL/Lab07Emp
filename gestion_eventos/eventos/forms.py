from django import forms
from .models import Evento, RegistroEvento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha']

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = []