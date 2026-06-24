from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modelo.models import Habitacion
from .serializers import HabitacionesSerializer


class HabitacionesListCreateView(ListCreateAPIView):
    serializer_class= HabitacionesSerializer
    def get_queryset(self):
        queryset = Habitacion.objects.all()
        habitacion = self.request.GET.get('habitacion_id')
        
        if habitacion:
            queryset = queryset.filter(tipo_id= habitacion)
            
        return queryset
    

class HabitacionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesSerializer
    

# Create your views here.
