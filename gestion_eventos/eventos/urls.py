from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:evento_id>/registrar/', views.registrar_en_evento, name='registrar_en_evento'),
]