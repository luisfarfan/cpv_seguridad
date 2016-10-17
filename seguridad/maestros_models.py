from __future__ import unicode_literals
from django.db import models
from relaciones_models import ReMenuPermisos


# Create your models here.

class MaeUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='ID_USUARIO')
    dni = models.CharField(db_column='DNI', max_length=8)
    ape_pat_per = models.CharField(
        db_column='APE_PAT_PER', max_length=35, blank=True, null=True)
    ape_mat_per = models.CharField(
        db_column='APE_MAT_PER', max_length=35, blank=True, null=True)
    nom_emp_per = models.CharField(
        db_column='NOM_EMP_PER', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    fec_nac_per = models.DateTimeField(
        db_column='FEC_NAC_PER', blank=True, null=True)
    email_insti = models.CharField(
        db_column='EMAIL_INSTI', max_length=50, blank=True, null=True)
    sex_emp_per = models.CharField(
        db_column='SEX_EMP_PER', max_length=1, blank=True, null=True)
    nom_completo = models.CharField(
        db_column='NOMBRE_COMPLETO', max_length=250, blank=True, null=True)
    usuario = models.CharField(
        db_column='USUARIO', max_length=20, blank=True, null=True)
    clave = models.CharField(
        db_column='CLAVE', max_length=20, blank=True, null=True)

    # proyectos_sistemas = models.ManyToManyField(ReProyectoSistemaMenu, through='ReUsuarioProyectoSistema')

    def __unicode__(self):
        return '%s , %s' % (self.dni, self.nom_emp_per)

    def save(self, *args, **kwargs):
        self.nom_completo = self.ape_pat_per + ' ' + \
                            self.ape_mat_per + ' ' + self.nom_emp_per
        return super(MaeUsuario, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'USUARIO'


class MaeProyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True, db_column='ID_PROYECTO')
    sigla_proy = models.CharField(
        db_column='SIGLA_PROY', max_length=20, blank=True, null=True)
    anio_proy = models.CharField(
        db_column='ANIO_PROY', max_length=4, blank=True, null=True)
    des_proy = models.CharField(
        db_column='DES_PROY', max_length=255, blank=True, null=True)
    tipo_proy = models.CharField(
        db_column='TIPO_PROY', max_length=1, blank=True, null=True)
    fec_inicio = models.DateTimeField(
        db_column='FEC_INICIO', blank=True, null=True)
    fec_final = models.DateTimeField(
        db_column='FEC_FINAL', blank=True, null=True)
    observacion = models.CharField(
        db_column='OBSERVACION', max_length=250, blank=True, null=True)
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
    cod_meta = models.CharField(db_column='COD_META', max_length=8, blank=True, null=True)
    sistemas = models.ManyToManyField(
        'MaeSistema', through='ReProyectoSistema')

    def __unicode__(self):
        return '%s , %s' % (self.id_proyecto, self.sigla_proy)

    class Meta:
        managed = True
        db_table = 'MAE_PROYECTO'


class MaeSistema(models.Model):
    id_sistema = models.AutoField(db_column='ID_SISTEMA', primary_key=True)
    des_sist = models.CharField(
        db_column='DES_SIST', max_length=100, blank=True, null=True)
    nom_sist = models.CharField(
        db_column='NOM_SIST', max_length=50, blank=True, null=True)
    codigo_sist = models.CharField(db_column='CODIGO_SISTEMA', max_length=20, blank=True, null=True)
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
        return '%s , %s' % (self.id_sistema, self.des_sist)

    class Meta:
        managed = True
        db_table = 'MAE_SISTEMA'


class MaePermiso(models.Model):
    id_permiso = models.AutoField(db_column='ID_PERMISO', primary_key=True)
    des_permiso = models.CharField(
        db_column='DES_PERMISO', max_length=100, blank=True, null=True)
    cod_permiso = models.CharField(
        db_column='COD_PERMISO', max_length=4, blank=True, null=True)
    nom_permiso = models.CharField(
        db_column='NOM_PERMISO', max_length=50, blank=True, null=True)
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
        return '%s , %s' % (self.cod_permiso, self.des_permiso)

    class Meta:
        managed = True
        db_table = 'MAE_PERMISO'
        unique_together = (('cod_permiso',))


class MaeRol(models.Model):
    id_rol = models.AutoField(db_column='ID_ROL', primary_key=True)
    des_rol = models.CharField(
        db_column='DES_ROL', max_length=100, blank=True, null=True)
    nom_rol = models.CharField(
        db_column='NOM_ROL', max_length=50, blank=True, null=True)
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
    menupermisos = models.ManyToManyField(
        ReMenuPermisos, through='ReMenuPermisosRol')

    def __unicode__(self):
        return '%s' % self.des_rol

    class Meta:
        managed = True
        db_table = 'MAE_ROL'
