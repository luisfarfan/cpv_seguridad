from rest_framework import  viewsets
from .relaciones_models import *
from serializer import *
from django.http import HttpResponse
from django.views import View
from django.core import serializers
# Create your views here.

# class ProyectoViewSet(viewsets.ModelViewSet):
#     queryset = Proyecto.objects.all()
#     serializer_class = ProyectoSerializer
#
# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuariosSerializer
#
# class SistemaViewSet(viewsets.ModelViewSet):
#     queryset = Sistema.objects.all()
#     serializer_class = SistemaSerializer
#
# class ProyectoSistemaViewSet(viewsets.ModelViewSet):
#     queryset = ProyectoSistema.objects.all()
#     serializer_class = ProyectoSistemaSerializer
#
# class UsuarioProyectoSistemaViewSet(viewsets.ModelViewSet):
#     queryset = UsuarioProyectoSistema.objects.all()
#     serializer_class = UsuarioProyectoSistemaSerializer
#
# class ProyectoSistemaView(View):
#
#     def get(self, request):
#         data = ProyectoSistema.objects.all()
#         json = serializers.serialize('json', data)
#         return HttpResponse(json, content_type='application/json')

