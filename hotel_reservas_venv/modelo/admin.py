from django.contrib import admin
from .models import Usuario,Reserva,Rol,RolUsuario,Factura,ReservaHabitacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(RolUsuario)
admin.site.register(Reserva)
admin.site.register(Factura)
admin.site.register(ReservaHabitacion)