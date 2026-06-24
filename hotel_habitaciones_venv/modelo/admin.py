from django.contrib import admin
from .models import Habitacion,TipoHabitacion,Servicio,TipoServicio

# Register your models here.
admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(Servicio)
admin.site.register(TipoServicio)