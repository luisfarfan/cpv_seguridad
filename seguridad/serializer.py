from seguridad.relaciones_models import *
from seguridad.maestros_models import *
from rest_framework import routers, serializers, viewsets


class MaeSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaeSistema
        #fields = ('id_sistema','des_sist','nom_sist','flag_activo','usr_creacion')


class MaeProyectoSerializer(serializers.ModelSerializer):
    #sistemas = MaeSistemaSerializer(many=True, read_only=True)
    class Meta:
        model = MaeProyecto
        #fields = ('id_proyecto','sigla_proy','anio_proy','des_proy','tipo_proy')


class MaeUsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeUsuario


class ProyectosbySistemaSerializer(serializers.ModelSerializer):
    sistemas = MaeSistemaSerializer(many=True, read_only=True)
    class Meta:
        model = MaeProyecto
        #fields = ('id_proyecto','sigla_proy','anio_proy','des_proy','tipo_proy','sistemas')
    """
    def create(self, validated_data):
        proyectos = validated_data.pop('proyectos')
        sistemas = MaeSistema.objects.create(**validated_data)
        for proyecto in proyectos:
            MaeProyecto.objects.create(sistemas=sistemas, **proyectos)
        return sistemas
    """

class MaePermisosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaePermiso
        fields = ('id_permiso','des_permiso','cod_permiso','nom_permiso','usr_creacion')


class MaeRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeRol


class ReProyectoSistemaSerializer(serializers.ModelSerializer):
    proyectos = MaeProyectoSerializer(many=True, read_only=True)
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
