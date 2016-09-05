from __future__ import unicode_literals
from django.db import models

class ViewPermisosMenuChild(models.Model):
    id_permisosusuario = models.IntegerField(primary_key=True, db_column='ID_PERMISOSUSUARIO')
    id_menu = models.IntegerField(db_column='ID_MENU')
    cod_permiso = models.CharField(db_column='COD_PERMISO', max_length=4)
    nom_permiso = models.CharField(db_column='NOM_PERMISO', max_length=15)
    des_rol = models.CharField(db_column='DES_ROL', max_length=50)
    id_usuario = models.IntegerField(db_column='ID_USUARIO')

    class Meta:
        managed = False
        db_table = 'permisos_menu_child'
        
