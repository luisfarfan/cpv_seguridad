from seguridad.relaciones_models import *
from seguridad.maestros_models import *
from rest_framework import routers, serializers, viewsets


class MaeProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeProyecto
        fields = ('id_proyecto','sigla_proy','anio_proy','des_proy','tipo_proy')


class MaeUsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeUsuario


class MaeSistemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeSistema
        fields = ('id_sistema','des_sist','nom_sist','flag_activo','usr_creacion')


class MaePermisosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaePermiso


class MaeRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaeRol


class ReProyectoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReProyectoSistema
        fields = ('id_proyecto_id','titulo_sistema_padre')


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
