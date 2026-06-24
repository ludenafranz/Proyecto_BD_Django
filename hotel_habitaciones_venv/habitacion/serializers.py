from rest_framework import serializers
from modelo.models import Servicio,TipoHabitacion,TipoServicio, Habitacion

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
        
class TipoHabitacionSerializer(serializers.ModelSerializer):
    servicios = serializers.SerializerMethodField()
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

    def get_servicios(self,obj):
        relaciones = TipoServicio.objects.filter(tipo_id=obj)
        return [r.servicio.nombre for r in relaciones]
    
class HabitacionesSerializer(serializers.ModelSerializer):
    tipo = TipoHabitacionSerializer()
    class Meta:
        model = Habitacion
        fields = '__all__'