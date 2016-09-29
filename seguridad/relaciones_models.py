from __future__ import unicode_literals
from maestros_models import *
from django.db import models
from django.utils.text import slugify


class ReProyectoSistema(models.Model):
    id_proyectosistema = models.AutoField(
        db_column='ID_PROYECTOSISTEMA', primary_key=True)
    id_proyecto = models.ForeignKey(
        'MaeProyecto', db_column="ID_PROYECTO", on_delete=models.CASCADE, related_name='proyectos')
    id_sistema = models.ForeignKey(
        'MaeSistema', db_column="ID_SISTEMA", on_delete=models.CASCADE, related_name='sistemas')
    usr_creacion = models.CharField(
        db_column='USR_CREACION', max_length=8, blank=True, null=True)
    fec_creacion = models.DateTimeField(
        db_column='FEC_CREACION', auto_now_add=True)
    usr_edicion = models.CharField(
        db_column='USR_EDICION', max_length=8, blank=True, null=True)
    fec_edicion = models.DateTimeField(
        db_column='FEC_EDICION', blank=True, null=True)
    titulo_sistema_padre = models.CharField(
        db_column = 'TITULO_SISTEMA_PADRE',max_length=50, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        super(ReProyectoSistema, self).save(*args, **kwargs)
        menu = ReMenu(id_proyectosistema=self, titulo=self.titulo_sistema_padre, nom_menu=self.titulo_sistema_padre,des_menu=self.titulo_sistema_padre)
        #super(ReMenu, menu).save(*args, **kwargs)
        #menu=ReMenu(id_proyectosistema=self.id_proyectosistema)
        menu.save()
        return self

    def __unicode__(self):
        return '%s , %s' % (self.id_proyecto, self.id_sistema)

    class Meta:
        managed = True
        db_table = 'TB_PROYECTO_SISTEMA'
        unique_together = (('id_proyecto', 'id_sistema'))


class ReMenu(models.Model):
    id_menu = models.AutoField(db_column='ID_MENU', primary_key=True)
    id_proyectosistema = models.ForeignKey(
        ReProyectoSistema, db_column='ID_PROYECTOSISTEMA')
    titulo = models.CharField(
        db_column='TITULO', max_length=50, blank=True, null=True)
    nom_menu = models.CharField(
        db_column='NOM_MENU', max_length=100, blank=True, null=True)
    des_menu = models.TextField(db_column='DES_MENU', blank=True)
    flag_activo = models.CharField(
        db_column='FLAG_ACTIVO', max_length=1, blank=True, null=True)
    flag_eliminado = models.CharField(
        db_column='FLAG_ELIMINADO', max_length=1, blank=True, null=True)
    usr_creacion = models.CharField(
        db_column='USR_CREACION', max_length=8, blank=True, null=True)
    fec_creacion = models.DateTimeField(
        db_column='FEC_CREACION', auto_now_add=True)
    usr_edicion = models.CharField(
        db_column='USR_EDICION', max_length=8, blank=True, null=True)
    fec_edicion = models.DateTimeField(
        db_column='FEC_EDICION', blank=True, null=True)
    url = models.CharField(
        db_column='URL', max_length=100, blank=True, null=True)
    slug = models.CharField(
        db_column='slug', max_length=100, blank=True, null=True)
    img = models.CharField(
        db_column='IMG', max_length=255, blank=True, null=True)
    padre_id = models.ForeignKey(
        'self', db_column='PADRE_ID', null=True, blank=True)

    def __unicode__(self):
        return '%s, %s' % (self.id_proyectosistema, self.nom_menu)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        return super(ReMenu, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'TB_MENU'


# class ReMenuRol(models.Model):
#     id_menurol = models.AutoField(db_column='ID_MENUROL', primary_key=True)
#     id_menu = models.ForeignKey(ReMenu, db_column='ID_MENU')
#     id_rol = models.ForeignKey(MaeRol, db_column='ID_ROL')
#     flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True, null=True)
#     flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True, null=True)
#     usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True, null=True)
#     fec_creacion = models.DateTimeField(db_column='FEC_CREACION', auto_now_add=True)
#     usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True, null=True)
#     fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)
#
#     def __unicode__(self):
#         return '%s , %s' % (self.id_menu, self.id_rol)
#
#     class Meta:
#         managed = True
#         db_table = 'TB_MENU_ROL'
#         unique_together = (('id_menu','id_rol'))


class ReMenuPermisos(models.Model):
    id_menupermisos = models.AutoField(
        db_column='ID_MENUPERMISOS', primary_key=True)
    id_menu = models.ForeignKey(ReMenu, db_column='ID_MENU')
    id_permiso = models.ForeignKey('MaePermiso', db_column='ID_PERMISO')
    flag_activo = models.CharField(
        db_column='FLAG_ACTIVO', max_length=1, blank=True, null=True)
    flag_eliminado = models.CharField(
        db_column='FLAG_ELIMINADO', max_length=1, blank=True, null=True)
    usr_creacion = models.CharField(
        db_column='USR_CREACION', max_length=8, blank=True, null=True)
    fec_creacion = models.DateTimeField(
        db_column='FEC_CREACION', auto_now_add=True)
    usr_edicion = models.CharField(
        db_column='USR_EDICION', max_length=8, blank=True, null=True)
    fec_edicion = models.DateTimeField(
        db_column='FEC_EDICION', blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.id_menu, self.id_permiso)

    class Meta:
        managed = True
        db_table = 'TB_PERMISOS_MENU'
        unique_together = (('id_menu', 'id_permiso'),)


class ReMenuPermisosRol(models.Model):
    id_menupermisosrol = models.AutoField(
        primary_key=True, db_column='ID_MENUPERMISOSROL')
    id_rol = models.ForeignKey(
        'MaeRol', db_column='ID_ROL', on_delete=models.CASCADE, related_name='roles')
    id_menupermisos = models.ForeignKey(
        ReMenuPermisos, db_column='ID_MENUPERMISOS', on_delete=models.CASCADE, related_name='remenupermisos')
    flag_activo = models.CharField(
        db_column='FLAG_ACTIVO', max_length=1, blank=True, null=True)
    flag_eliminado = models.CharField(
        db_column='FLAG_ELIMINADO', max_length=1, blank=True, null=True)
    usr_creacion = models.CharField(
        db_column='USR_CREACION', max_length=8, blank=True, null=True)
    fec_creacion = models.DateTimeField(
        db_column='FEC_CREACION', auto_now_add=True)
    usr_edicion = models.CharField(
        db_column='USR_EDICION', max_length=8, blank=True, null=True)
    fec_edicion = models.DateTimeField(
        db_column='FEC_EDICION', blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.id_menupermisos, self.id_rol)

    class Meta:
        managed = True
        db_table = 'TB_MENU_PERMISOS_ROL'
        unique_together = (('id_rol', 'id_menupermisos',))


class ReMenuPermisosRolUsuario(models.Model):
    id_permisosusuario = models.AutoField(
        primary_key=True, db_column='ID_PERMISOSUSUARIO')
    id_menupermisosrol = models.ForeignKey(
        ReMenuPermisosRol, db_column='ID_MENUPERMISOSROL')
    id_usuario = models.ForeignKey('MaeUsuario', db_column='ID_USUARIO')
    flag_activo = models.CharField(
        db_column='FLAG_ACTIVO', max_length=1, blank=True, null=True)
    flag_eliminado = models.CharField(
        db_column='FLAG_ELIMINADO', max_length=1, blank=True, null=True)
    usr_creacion = models.CharField(
        db_column='USR_CREACION', max_length=8, blank=True, null=True)
    fec_creacion = models.DateTimeField(
        db_column='FEC_CREACION', auto_now_add=True)
    usr_edicion = models.CharField(
        db_column='USR_EDICION', max_length=8, blank=True, null=True)
    fec_edicion = models.DateTimeField(
        db_column='FEC_EDICION', blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.id_menupermisosrol, self.id_usuario)

    class Meta:
        managed = True
        db_table = 'TB_MENU_PERMISOS_ROL_USUARIO'
        unique_together = (('id_menupermisosrol', 'id_usuario'))
