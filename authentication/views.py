from django.shortcuts import render
from seguridad.maestros_models import MaeUsuario
from api_angular.views import get_session
from seguridad.helpers import json_serial
from django.http import HttpResponse
import json


def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        user = list(MaeUsuario.objects.filter(
            usuario=usuario, clave=clave).values())

        if user:
            sesion = get_session(user[0]['id_usuario'])
            user[0]['detalle']=sesion
        else:
            user = []

    return HttpResponse(json.dumps(user, default=json_serial), content_type='application/json')
