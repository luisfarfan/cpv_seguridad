from seguridad.relaciones_models import *
from seguridad.maestros_models import *
from rest_framework import routers, serializers, viewsets


class MaeProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeProyecto


class MaeUsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeUsuario


class MaeSistemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeSistema


class MaePermisosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaePermiso


class MaeRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeRol


class ReProyectoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReProyectoSistema


class ReMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReMenu


class ReMenuPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReMenuPermisos


class ReMenuPermisosRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReMenuPermisosRol


class ReMenuPermisosRolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReMenuPermisosRolUsuario
