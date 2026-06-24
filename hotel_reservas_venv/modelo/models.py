# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class MetodoPago(models.TextChoices):
    # NOMBRE = 'VALOR_EN_BASE_DATOS', 'Texto para formularios/Admin'
    EFECTIVO = 'efectivo', 'Efectivo'
    TARJETA = 'tarjeta', 'Tarjeta'
    TRANSFERENCIA = 'transferencia', 'Transferencia'

class Factura(models.Model):
    factura_id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    reserva = models.ForeignKey('Reserva', models.DO_NOTHING, blank=True, null=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_emision = models.DateField()
    metodo_pago = models.TextField(choices=MetodoPago, default= MetodoPago.EFECTIVO) 

    class Meta:
        managed = False
        db_table = 'factura'
    def __str__(self):
        return f"{self.numero}"

class EstadoReserva(models.TextChoices):
    CONFIRMADA = 'confirmada', 'Confirmada'
    CANCELADA = 'cancelada', 'Cancelada'
    FINALIZADA = 'finalizada', 'Finalizada'
    PENDIENTE = 'pendiente', 'Pendiente'

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    cedula = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='cedula', blank=True, null=True)
    fecha_reserva = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.TextField(choices=EstadoReserva, default= EstadoReserva.PENDIENTE)

    class Meta:
        managed = False
        db_table = 'reserva'
    def __str__(self):
        return f"{self.reserva_id}"


class ReservaHabitacion(models.Model):
    reserva_habitacion_id = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reserva, models.DO_NOTHING, blank=True, null=True)
    habitacion_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reserva_habitacion'
    def __str__(self):
        return f"{self.reserva} - {self.habitacion_id}"


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'
    def __str__(self):
        return f"{self.nombre}"

class RolUsuario(models.Model):
    rol_usuario_id = models.AutoField(primary_key=True)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, blank=True, null=True)
    cedula = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='cedula', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol_usuario'


class Usuario(models.Model):
    cedula = models.CharField(primary_key=True, max_length=15)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"
