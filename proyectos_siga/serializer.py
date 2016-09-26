from rest_framework import serializers
from models import ProyectosSiga


class ProyectosSigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectosSiga
        fields = ('id_proyecto','desc_proyecto','codi_Meta','modalidad','CODI_DEPE_TDE','annio_meta','objetivo')
