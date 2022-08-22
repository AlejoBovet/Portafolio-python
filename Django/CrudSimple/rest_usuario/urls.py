from django.urls import path
from rest_usuario.views import detalle_Blog, lista_Blog
from . import views
from rest_usuario.viewsLogin import login

urlpatterns=[

 path('api/',views.lista_Blog, name='lista_Blog'),

path('detalle_Blog/<id>',views.detalle_Blog, name='detalle_Blog'),
path('login/',login, name='login'),
]