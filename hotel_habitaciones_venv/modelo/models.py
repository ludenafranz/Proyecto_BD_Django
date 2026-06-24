# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class EstadoHabitacion(models.TextChoices):
    # NOMBRE = 'VALOR_EN_BASE_DATOS', 'Texto para formularios/Admin'
    DISPONIBLE = 'disponible', 'Disponibles'
    OCUPADA = 'ocupada', 'Ocupada'
    MANTENIMIENTO = 'mantenimiento', 'Mantenimiento'
    LIMPIEZA = 'limpieza', 'Limpieza'

class Habitacion(models.Model):
    habitacion_id = models.AutoField(primary_key=True)
    numero = models.CharField(unique=True, max_length=10)
    tipo = models.ForeignKey('TipoHabitacion', models.DO_NOTHING, blank=True, null=True)
    piso = models.IntegerField()
    estado = models.TextField(choices=EstadoHabitacion, default= EstadoHabitacion.DISPONIBLE) 

    class Meta:
        managed = False
        db_table = 'habitacion'
    def __str__(self):
        return f"{self.numero}"
    def __str__(self):
        return f"Habitacion: {self.numero}"


class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'servicio'
    def __str__(self):
        return f"{self.nombre}"


class TipoHabitacion(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion = models.TextField()
    capacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_habitacion'
    def __str__(self):
        return f"{self.nombre}"


class TipoServicio(models.Model):
    tipo_servicio_id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio, models.DO_NOTHING, blank=True, null=True)
    tipo = models.ForeignKey(TipoHabitacion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'
    def __str__(self):
        return f"{self.servicio.nombre} - {self.tipo.nombre}"
