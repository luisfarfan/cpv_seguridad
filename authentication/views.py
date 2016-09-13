from django.shortcuts import render
from seguridad.maestros_models import MaeUsuario
from api_angular.views import get_session,get_routes
from seguridad.helpers import json_serial
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login(request):
    user = False
    if(request.method == 'GET'):

        username = request.GET.get('username', False)
        contrasena = request.GET.get('clave', False)
        user = list(MaeUsuario.objects.filter(usuario=username, clave=contrasena).values())

        if user:
            sesion = get_session(user[0]['id_usuario'])
            user[0]['detalle'] = sesion
            user[0]['routes'] = get_routes(user[0]['id_usuario'])
        else:
            user = False

    return HttpResponse(json.dumps(user, default=json_serial), content_type='application/json')
