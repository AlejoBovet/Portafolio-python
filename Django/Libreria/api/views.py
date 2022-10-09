
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from libreria.models import Libro
import json



# Create your views here.


class LibrosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    
    def get(self, request, id=0):
        global Libro
        if(id > 0):
            Libross=list(Libro.objects.filter(id=id).values())
            if len(Libross)>0:
                libro = Libross[0]
                datos ={'message': "success", "Libro": libro}
            else:
                datos ={'message': "Libros no encontrados"}
            return JsonResponse(datos)  
        else:
            Libross=list(Libro.objects.values())
            if len(Libross) > 0:
                datos = {'message': "success", "Libros": libro}  
            else:
                datos ={'message': "Libros no encontrados"}
            return JsonResponse(datos)

    def post(self,request):
        global Libro    
        jd= json.loads(request.body)
        Libro.objects.create(titulo=jd['titulo'], imagen=jd['imagen'], descripcion=jd['descripcion'])
        datos= {'message': 'success'}  
        return JsonResponse(datos)


    def put(self,request,id):
        global Libro
        jd=json.loads(request.body)
        Datos= list(Libro.objects.filter(id=id).values())
        if len(Datos) > 0:
            libro=Libro.objects.get(id=id)
            libro.titulo=jd['titulo']
            libro.imagen=jd['imagen']
            libro.descripcion=jd['descripcion']
            libro.save()    
            datos = {'  message': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'message': 'libro not found....'}    
        return JsonResponse(datos)


    def delete(self,request, id):
        global Libro
        libro = list(Libro.objects.filter(id=id).values())
        if len(libro) > 0:
            Libro.objects.filter(id=id).delete()
            datos = {'message': 'success'} 
        else:
            datos = {'message': 'libro not found....'}
        return JsonResponse(datos)

     


