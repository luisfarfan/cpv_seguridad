from rest_framework import viewsets
from .relaciones_models import *
from serializer import *
from django.http import HttpResponse
from django.views import View
from django.core import serializers


# Create your views here.

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = MaeProyecto.objects.all()
    serializer_class = MaeProyectoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = MaeUsuario.objects.all()
    serializer_class = MaeUsuariosSerializer


class SistemaViewSet(viewsets.ModelViewSet):
    queryset = MaeSistema.objects.all()
    serializer_class = MaeSistemaSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = MaeRol.objects.all()
    serializer_class = MaeRolesSerializer


class PermisosViewSet(viewsets.ModelViewSet):
    queryset = MaePermiso.objects.all()
    serializer_class = MaePermisosSerializer


class ProyectoSistemaViewSet(viewsets.ModelViewSet):
    queryset = ReProyectoSistema.objects.all()
    serializer_class = ReProyectoSistemaSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = ReMenu.objects.all()
    serializer_class = ReMenuSerializer


class MenuPermisosViewSet(viewsets.ModelViewSet):
    queryset = ReMenuPermisos.objects.all()
    serializer_class = ReMenuPermisosSerializer


class MenuPermisosRolViewSet(viewsets.ModelViewSet):
    queryset = ReMenuPermisosRol.objects.all()
    serializer_class = ReMenuPermisosRolSerializer


class MenuPermisosRolUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ReMenuPermisosRolUsuario.objects.all()
    serializer_class = ReMenuPermisosRolUsuarioSerializer
