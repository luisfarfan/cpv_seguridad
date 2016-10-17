from rest_framework import serializers
from models import ProyectosSiga


class ProyectosSigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectosSiga
        #fields = ('id','annio_meta','codi_meta','cod_proyecto','desc_proyecto','CODI_DEPE_TDE','codi_depe_apro','sigla')
