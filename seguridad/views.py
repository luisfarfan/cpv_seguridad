from rest_framework import viewsets
from .relaciones_models import *
from serializer import *
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
import json
import logging
from helpers import json_serial


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


def procedure(request):
    menu = set_permissions_to_menu_child(permissions(), menu_parent_child())

    return HttpResponse(json.dumps(menu, default=json_serial), content_type='application/json')


def permissions():
    from .db_views import ViewPermisosMenuChild
    permisos = list(ViewPermisosMenuChild.objects.filter(id_usuario=3).values(
        'cod_permiso', 'nom_permiso', 'des_rol', 'id_menu'))

    return permisos


def menu_parent_child():
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute('exec getMenubyUser %s', [3])
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))

    return menu


def set_permissions_to_menu_child(permissions, menu):
    padres = []
    hijos = []
    for k, v in enumerate(menu):
        if menu[k]['PADRE_ID'] == None:
            padres.append(menu[k])
        else:
            hijos.append(menu[k])

    for k, v in enumerate(hijos):
        permisos = []
        for kk, vv in enumerate(permissions):
            if vv['id_menu'] == v['ID_MENU']:
                permisos.append(dict(permissions[kk]))
                hijos[k]['permisos'] = permisos

    for k, v in enumerate(padres):
        listadict = []
        for kk, vv in enumerate(hijos):
            if hijos[kk]['PADRE_ID'] == padres[k]['ID_MENU']:
                listadict.append(dict(hijos[kk]))
                padres[k]['hijos'] = listadict

    return padres
