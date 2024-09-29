from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Evento, RegistroEvento

# Crear un nuevo evento
def crear_evento(titulo, descripcion, fecha, organizador_id):
    organizador = User.objects.get(id=organizador_id)
    evento = Evento.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        fecha=fecha,
        organizador=organizador
    )
    return evento

# Registrar un usuario en un evento
def registrar_usuario_en_evento(usuario_id, evento_id):
    usuario = User.objects.get(id=usuario_id)
    evento = Evento.objects.get(id=evento_id)
    registro = RegistroEvento.objects.create(usuario=usuario, evento=evento)
    return registro

# Consultar usuarios registrados en un evento específico
def usuarios_registrados_en_evento(evento_id):
    evento = Evento.objects.get(id=evento_id)
    return evento.registros.count()

# Consultar eventos este mes
def eventos_este_mes():
    hoy = timezone.now()
    inicio_mes = hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    fin_mes = (inicio_mes + timedelta(days=32)).replace(day=1) - timedelta(seconds=1)
    return Evento.objects.filter(fecha__range=(inicio_mes, fin_mes)).count()

# Consultar usuarios más activos
def usuarios_mas_activos(top_n=5):
    return User.objects.annotate(num_eventos=models.Count('eventos_registrados')).order_by('-num_eventos')[:top_n]

# Consultar eventos organizados por un usuario
def eventos_organizados_por_usuario(usuario_id):
    return Evento.objects.filter(organizador_id=usuario_id).count()

# Actualizar información de un evento
def actualizar_evento(evento_id, **kwargs):
    evento = Evento.objects.get(id=evento_id)
    for key, value in kwargs.items():
        setattr(evento, key, value)
    evento.save()
    return evento

# Eliminar un evento
def eliminar_evento(evento_id):
    evento = Evento.objects.get(id=evento_id)
    evento.delete()