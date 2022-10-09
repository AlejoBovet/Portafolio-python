from django import views
from django.urls import path
from api.views import LibrosView

urlpatterns = [
    path('librosalmacenados/', LibrosView.as_view(), name='librosAlmacenados_list'),
    path('librosalmacenados/<int:id>', LibrosView.as_view(), name='librosAlmacenados_process'), 
]

