from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Libro, Profile
from .forms import LibroForm
from django.http import JsonResponse
from django.views import View
from django.contrib import messages


# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')
    
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario} )

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario{username}creado') 
            return redirect ('inicio')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'Users/register.html', context) 

