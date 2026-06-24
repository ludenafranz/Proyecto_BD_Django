from django.urls import path
from . import views

urlpatterns = [
    path('guardar/', views.guardarReserva, name='guardar_reserva'),

]