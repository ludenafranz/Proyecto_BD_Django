from django.urls import path

from .views import HabitacionDetailView,HabitacionesListCreateView

urlpatterns = [
    path('habitacion/', HabitacionesListCreateView.as_view() ,name='habitaciones_list_create'),
    path('habitacion/<int:pk>/', HabitacionDetailView.as_view() ,name='habitaciones_details'),
]