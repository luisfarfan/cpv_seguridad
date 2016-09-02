from rest_framework import viewsets
from .relaciones_models import *
from serializer import *
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
import json
import logging
from datetime import datetime


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


def get(request):
    import json

    padres = list(ReMenu.objects.filter(padre_id__isnull=True).values())
    items = list(ReMenu.objects.filter(padre_id__isnull=False).values())
    for k, v in enumerate(padres):
        lista_dict = []
        for key, value in enumerate(items):
            if value['padre_id_id'] == v['id_menu']:
                lista_dict.append(dict(value))
                padres[k]['hijos'] = lista_dict

    # return HttpResponse(padres)
    return HttpResponse(json.dumps(padres, default=json_serial),content_type='application/json')
    # return HttpResponse(json.dumps(menu, default=json_serial), content_type='application/json')


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")

def procedure(request):
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute('exec getMenubyUser %s', [3])
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    return HttpResponse(results)
    #return HttpResponse(json.dumps(results, default=json_serial), content_type='application/json')