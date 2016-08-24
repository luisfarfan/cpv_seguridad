from seguridad.relaciones_models import *
from rest_framework import routers, serializers, viewsets

# class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Proyecto
#
# class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Usuario
#
# class SistemaSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Sistema
#
# class ProyectoSistemaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProyectoSistema
#
# class UsuarioProyectoSistemaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsuarioProyectoSistema
