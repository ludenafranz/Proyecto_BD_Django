import requests
from django.shortcuts import render,redirect
from django.contrib import messages
from modelo.models import Reserva, Usuario, ReservaHabitacion,EstadoReserva
from datetime import date,datetime

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def listarHabitaciones():
    url = "http://127.0.0.1:8001/habitaciones/habitacion/"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        return[]
    except requests.exceptions.RequestException:
        return[]

def guardarReserva(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        fecha_reserva = date.today()
        fecha_inicio_str = request.POST.get('fecha_inicio')
        fecha_fin_str = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        habitaciones_id = request.POST.getlist('habitaciones')
        
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, "El formato de las fechas es inválido.")
            return redirect('guardar_reserva')  # Cambia por el nombre de tu URL de origen
        
        if fecha_fin < fecha_inicio or fecha_inicio < fecha_reserva:
            messages.error(request, "Fechas Incorrectas.")
            return redirect('guardar_reserva')
        
        usuario = Usuario.objects.get(cedula=cedula)
        
        reserva = Reserva.objects.create(
            cedula = usuario,
            fecha_reserva = fecha_reserva,
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            estado = estado
        )
        
        for habid in habitaciones_id:
            ReservaHabitacion.objects.create(
                reserva = reserva,
                habitacion_id = habid
            )
        messages.success(request, "Reserva guardada exitosamente.")
        redirect('guardar_reserva')
    
    usuarios = Usuario.objects.all()
    
    contexto = {
        'usuarios':usuarios,
        'habitaciones': listarHabitaciones(),
        'estados': EstadoReserva.choices
    }

    return render(request, 'GuardarReserva.html', contexto)

