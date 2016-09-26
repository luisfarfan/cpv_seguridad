from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cpvapp.utils import JSONResponse
from models import ProyectosSiga
from serializer import ProyectosSigaSerializer

@csrf_exempt
def proyectossiga_list(request):
    if request.method == 'GET':
        proyectossiga = ProyectosSiga.objects.all()
        serializer = ProyectosSigaSerializer(proyectossiga, many=True)
        return JSONResponse(serializer.data)
    else:
        return HttpResponse(status=403)

@csrf_exempt
def proyectossiga_detail(request,pk):
    try:
        proyectossiga = ProyectosSiga.objects.get(pk=pk)
    except ProyectosSiga.DoesNotExist:
        return JSONResponse({'msj':'no existe pk'})

    if request.method == 'GET':
        serializer = ProyectosSigaSerializer(proyectossiga)
        return JSONResponse(serializer.data)
    else:
        return HttpResponse(status=403)
