from __future__ import unicode_literals

from django.db import models


# Create your models here.
# class ProyectosSiga(models.Model):
#     id = models.IntegerField(primary_key=True, db_column='id')
#     annio_meta =  models.CharField(db_column='annio_meta',max_length=4, blank=True, null=True)
#     codi_meta = models.CharField(db_column='codi_meta', max_length=4, blank=True, null=True)
#     cod_proyecto = models.CharField(db_column='cod_proyecto', max_length=4,blank=True, null=True)
#     desc_proyecto = models.CharField(db_column='desc_proyecto', max_length=255, blank=True, null=True)
#     CODI_DEPE_TDE = models.CharField(db_column='CODI_DEPE_TDE', max_length=4, blank=True, null=True)
#     codi_depe_apro = models.CharField(db_column='codi_depe_apro', max_length=4, blank=True, null=True)
#     sigla = models.CharField(db_column='sigla', max_length=50, blank=True, null=True)
#
#     def __unicode__(self):
#         return '%s , %s' % (self.codi_meta, self.desc_proyecto)
#
#     class Meta:
#         managed = False
#         db_table = 'V_PROYECTOS_SIGA'

class ProyectosSiga(models.Model):
    id_proyecto = models.AutoField(primary_key=True, db_column='id_Proyecto')
    desc_proyecto = models.CharField(db_column='desc_Proyecto', max_length=255, blank=True, null=True)
    cod_proyecto = models.CharField(db_column='cod_Proyecto', max_length=4, blank=True, null=True)
    codi_Meta = models.CharField(db_column='codi_Meta', max_length=4, blank=True, null=True)
    modalidad = models.CharField(db_column='modalidad', max_length=2, blank=True, null=True)
    CODI_DEPE_TDE = models.CharField(db_column='CODI_DEPE_TDE', max_length=4, blank=True, null=True)
    annio_meta = models.CharField(db_column='annio_Meta', max_length=4, blank=True, null=True)
    objetivo = models.CharField(db_column='objetivo', max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.codi_Meta, self.desc_proyecto)

    class Meta:
        managed = False
        db_table = 'PROYECTOS_SIGA'
