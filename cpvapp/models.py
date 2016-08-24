# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MaeOpcion(models.Model):
    tipo_opcion_id = models.IntegerField(db_column='TIPO_OPCION_ID')  # Field name made lowercase.
    nom_opcion = models.CharField(db_column='NOM_OPCION', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    des_opcion = models.CharField(db_column='DES_OPCION', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    opcion_id = models.IntegerField(db_column='OPCION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_OPCION'


class MaePermiso(models.Model):
    id_permiso = models.AutoField(db_column='ID_PERMISO', primary_key=True)  # Field name made lowercase.
    des_permiso = models.CharField(db_column='DES_PERMISO', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    cod_permiso = models.CharField(db_column='COD_PERMISO', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    nom_permiso = models.CharField(db_column='NOM_PERMISO', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_PERMISO'


class MaeProyecto(models.Model):
    id_proyecto = models.AutoField(db_column='ID_PROYECTO', primary_key=True)  # Field name made lowercase.
    sigla_proy = models.CharField(db_column='SIGLA_PROY', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    anio_proy = models.CharField(db_column='ANIO_PROY', max_length=4, blank=True,
                                 null=True)  # Field name made lowercase.
    des_proy = models.CharField(db_column='DES_PROY', max_length=60, blank=True,
                                null=True)  # Field name made lowercase.
    tipo_proy = models.CharField(db_column='TIPO_PROY', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    fec_inicio = models.DateTimeField(db_column='FEC_INICIO', blank=True, null=True)  # Field name made lowercase.
    fec_final = models.DateTimeField(db_column='FEC_FINAL', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='OBSERVACION', max_length=250, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_PROYECTO'


class MaeRol(models.Model):
    id_rol = models.AutoField(db_column='ID_ROL', primary_key=True)  # Field name made lowercase.
    des_rol = models.CharField(db_column='DES_ROL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nom_rol = models.CharField(db_column='NOM_ROL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_ROL'


class MaeSistema(models.Model):
    id_sistema = models.AutoField(db_column='ID_SISTEMA', primary_key=True)  # Field name made lowercase.
    des_sist = models.CharField(db_column='DES_SIST', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.
    nom_sist = models.CharField(db_column='NOM_SIST', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_SISTEMA'


class MaeTipoOpcion(models.Model):
    tipo_opcion_id = models.IntegerField(db_column='TIPO_OPCION_ID')  # Field name made lowercase.
    nom_tipo_opcion = models.CharField(db_column='NOM_TIPO_OPCION', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    des_tipo_opcion = models.CharField(db_column='DES_TIPO_OPCION', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_TIPO_OPCION'


class MaeUsuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    ape_pat_per = models.CharField(db_column='APE_PAT_PER', max_length=35, blank=True,
                                   null=True)  # Field name made lowercase.
    ape_mat_per = models.CharField(db_column='APE_MAT_PER', max_length=35, blank=True,
                                   null=True)  # Field name made lowercase.
    nom_emp_per = models.CharField(db_column='NOM_EMP_PER', max_length=35, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_nac_per = models.DateTimeField(db_column='FEC_NAC_PER', blank=True, null=True)  # Field name made lowercase.
    email_insti = models.CharField(db_column='EMAIL_INSTI', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    sex_emp_per = models.CharField(db_column='SEX_EMP_PER', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CLAVE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ult_logeo = models.DateTimeField(db_column='ULT_LOGEO', blank=True, null=True)  # Field name made lowercase.
    es_super = models.CharField(db_column='ES_SUPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    no_cambio = models.CharField(db_column='NO_CAMBIO', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAE_USUARIO'


class TbAmbito(models.Model):
    id_ambito = models.CharField(db_column='ID_AMBITO', max_length=18)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=18, blank=True,
                                   null=True)  # Field name made lowercase.
    descripcion_variable = models.CharField(db_column='DESCRIPCION_VARIABLE', max_length=18, blank=True,
                                            null=True)  # Field name made lowercase.
    padre_id = models.CharField(db_column='PADRE_ID', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.
    id_dis_geo = models.ForeignKey('TbDistribucionGeografica', models.DO_NOTHING,
                                   db_column='ID_DIS_GEO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_AMBITO'
        unique_together = (('id_ambito', 'id_dis_geo'),)


class TbAmbitoUsuario(models.Model):
    id_ambito = models.ForeignKey(TbAmbito, models.DO_NOTHING, db_column='ID_AMBITO')  # Field name made lowercase.
    id_dis_geo = models.ForeignKey(TbAmbito, models.DO_NOTHING, db_column='ID_DIS_GEO')  # Field name made lowercase.
    id_usuario = models.CharField(db_column='ID_USUARIO', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_AMBITO_USUARIO'
        unique_together = (('id_ambito', 'id_dis_geo', 'id_usuario'),)


class TbBd(models.Model):
    servidor_id = models.CharField(db_column='SERVIDOR_ID', max_length=18)  # Field name made lowercase.
    servicio_id = models.CharField(db_column='SERVICIO_ID', max_length=18)  # Field name made lowercase.
    bd_id = models.CharField(db_column='BD_ID', max_length=18)  # Field name made lowercase.
    nom_bd = models.CharField(db_column='NOM_BD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_BD'
        unique_together = (('bd_id', 'servidor_id', 'servicio_id'),)


class TbDistribucionGeografica(models.Model):
    id_dis_geo = models.CharField(db_column='ID_DIS_GEO', primary_key=True, max_length=18)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=18, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_DISTRIBUCION_GEOGRAFICA'


class TbIpDelimitado(models.Model):
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    ip_delimitado_id = models.CharField(db_column='IP_DELIMITADO_ID', max_length=18)  # Field name made lowercase.
    rango_inicio = models.CharField(db_column='RANGO_INICIO', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    rango_fin = models.CharField(db_column='RANGO_FIN', max_length=40, blank=True,
                                 null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='MOTIVO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    id_sistema = models.IntegerField(db_column='ID_SISTEMA')  # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_PROYECTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_IP_DELIMITADO'
        unique_together = (('ip_delimitado_id', 'id_sistema', 'id_proyecto'),)


class TbMetas(models.Model):
    anno_ejec_eje = models.CharField(db_column='ANNO_EJEC_EJE', max_length=4)  # Field name made lowercase.
    secu_ejec_cin = models.CharField(db_column='SECU_EJEC_CIN', max_length=4)  # Field name made lowercase.
    secu_func_sfu = models.CharField(db_column='SECU_FUNC_SFU', max_length=4)  # Field name made lowercase.
    codi_func_fun = models.CharField(db_column='CODI_FUNC_FUN', max_length=2)  # Field name made lowercase.
    codi_prog_prg = models.CharField(db_column='CODI_PROG_PRG', max_length=3)  # Field name made lowercase.
    csub_prog_spr = models.CharField(db_column='CSUB_PROG_SPR', max_length=4)  # Field name made lowercase.
    acti_proy_acp = models.CharField(db_column='ACTI_PROY_ACP', max_length=7)  # Field name made lowercase.
    codi_comp_com = models.CharField(db_column='CODI_COMP_COM', max_length=7)  # Field name made lowercase.
    codi_meta_sfu = models.CharField(db_column='CODI_META_SFU', max_length=5)  # Field name made lowercase.
    codi_fina_fin = models.CharField(db_column='CODI_FINA_FIN', max_length=5)  # Field name made lowercase.
    desc_meta_sfu = models.CharField(db_column='DESC_META_SFU', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    cant_meta_sfu = models.DecimalField(db_column='CANT_META_SFU', max_digits=22, decimal_places=0, blank=True,
                                        null=True)  # Field name made lowercase.
    codi_unid_med = models.CharField(db_column='CODI_UNID_MED', max_length=3, blank=True,
                                     null=True)  # Field name made lowercase.
    codi_depa_dpt = models.CharField(db_column='CODI_DEPA_DPT', max_length=2, blank=True,
                                     null=True)  # Field name made lowercase.
    codi_prov_tpr = models.CharField(db_column='CODI_PROV_TPR', max_length=2, blank=True,
                                     null=True)  # Field name made lowercase.
    codi_depe_tde = models.CharField(db_column='CODI_DEPE_TDE', max_length=4, blank=True,
                                     null=True)  # Field name made lowercase.
    tipo_ppto_tpr = models.CharField(db_column='TIPO_PPTO_TPR', max_length=4, blank=True,
                                     null=True)  # Field name made lowercase.
    codi_inst_ins = models.CharField(db_column='CODI_INST_INS', max_length=8, blank=True,
                                     null=True)  # Field name made lowercase.
    abrev_meta_sfu = models.CharField(db_column='ABREV_META_SFU', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    codi_depe_secun = models.CharField(db_column='CODI_DEPE_SECUN', max_length=4, blank=True,
                                       null=True)  # Field name made lowercase.
    tipo_meta_act = models.CharField(db_column='TIPO_META_ACT', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_METAS'
        unique_together = (('anno_ejec_eje', 'secu_ejec_cin', 'secu_func_sfu', 'codi_func_fun', 'csub_prog_spr',
                            'codi_prog_prg', 'acti_proy_acp', 'codi_comp_com', 'codi_meta_sfu', 'codi_fina_fin'),)


class TbPermisosMenu(models.Model):
    id_proyecto = models.ForeignKey('TbProySistMenu', models.DO_NOTHING,
                                    db_column='ID_PROYECTO')
    id_sistema = models.ForeignKey('TbProySistMenu', models.DO_NOTHING,
                                   db_column='ID_SISTEMA')
    id_menu = models.ForeignKey('TbProySistMenu', models.DO_NOTHING, db_column='ID_MENU')
    id_permiso = models.ForeignKey(MaePermiso, models.DO_NOTHING, db_column='ID_PERMISO')
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_PERMISOS_MENU'
        # unique_together = (('id_proyecto', 'id_sistema', 'id_menu', 'id_permiso'),)


class TbPermisoEspecial(models.Model):
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.CharField(db_column='ID_USUARIO', max_length=8)  # Field name made lowercase.
    id_menu = models.CharField(db_column='ID_MENU', max_length=18)  # Field name made lowercase.
    id_sistema = models.IntegerField(db_column='ID_SISTEMA')  # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_PROYECTO')  # Field name made lowercase.
    id_permiso = models.IntegerField(db_column='ID_PERMISO')  # Field name made lowercase.
    id_rol = models.IntegerField(db_column='ID_ROL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PERMISO_ESPECIAL'


class TbPermisoRolSistema(models.Model):
    id_proyecto = models.ForeignKey(TbPermisosMenu, models.DO_NOTHING,
                                    db_column='ID_PROYECTO')  # Field name made lowercase.
    id_sistema = models.ForeignKey(TbPermisosMenu, models.DO_NOTHING,
                                   db_column='ID_SISTEMA')  # Field name made lowercase.
    id_menu = models.ForeignKey(TbPermisosMenu, models.DO_NOTHING, db_column='ID_MENU')  # Field name made lowercase.
    id_rol = models.ForeignKey('TbRolSistMenu', models.DO_NOTHING, db_column='ID_ROL')  # Field name made lowercase.
    id_permiso = models.ForeignKey(TbPermisosMenu, models.DO_NOTHING,
                                   db_column='ID_PERMISO')  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PERMISO_ROL_SISTEMA'
        # unique_together = (
        # ('id_proyecto', 'id_proyecto', 'id_sistema', 'id_sistema', 'id_menu', 'id_menu', 'id_rol', 'id_permiso'),)


class TbPermisoUsuario(models.Model):
    id_proyecto = models.ForeignKey(TbPermisoRolSistema, models.DO_NOTHING,
                                    db_column='ID_PROYECTO')  # Field name made lowercase.
    id_sistema = models.ForeignKey(TbPermisoRolSistema, models.DO_NOTHING,
                                   db_column='ID_SISTEMA')  # Field name made lowercase.
    id_menu = models.ForeignKey(TbPermisoRolSistema, models.DO_NOTHING,
                                db_column='ID_MENU')  # Field name made lowercase.
    id_rol = models.ForeignKey(TbPermisoRolSistema, models.DO_NOTHING, db_column='ID_ROL')  # Field name made lowercase.
    id_permiso = models.ForeignKey(TbPermisoRolSistema, models.DO_NOTHING,
                                   db_column='ID_PERMISO')  # Field name made lowercase.
    id_usuario = models.ForeignKey(MaeUsuario, models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    fec_inicio = models.DateTimeField(db_column='FEC_INICIO', blank=True, null=True)  # Field name made lowercase.
    fec_final = models.DateTimeField(db_column='FEC_FINAL', blank=True, null=True)  # Field name made lowercase.
    tipo_opcion_id = models.IntegerField(db_column='TIPO_OPCION_ID')  # Field name made lowercase.
    opcion_id = models.IntegerField(db_column='OPCION_ID')  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PERMISO_USUARIO'
        # unique_together = (('id_proyecto', 'id_sistema', 'id_menu', 'id_rol', 'id_permiso', 'id_usuario'),)


class TbProyectoDistribucionGeografica(models.Model):
    id_proyecto = models.IntegerField(db_column='ID_PROYECTO')  # Field name made lowercase.
    id_dis_geo = models.ForeignKey(TbDistribucionGeografica, models.DO_NOTHING,
                                   db_column='ID_DIS_GEO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PROYECTO_DISTRIBUCION_GEOGRAFICA'
        # unique_together = (('id_proyecto', 'id_dis_geo'),)


class TbProySistema(models.Model):
    id_proyecto = models.ForeignKey(MaeProyecto, models.DO_NOTHING,
                                    db_column='ID_PROYECTO', primary_key=True, related_name='proyecto_idproyecto')  # Field name made lowercase.
    id_sistema = models.ForeignKey(MaeSistema, models.DO_NOTHING, db_column='ID_SISTEMA',primary_key=True, related_name='sistema_idsistema')  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_opcion_id = models.IntegerField(db_column='TIPO_OPCION_ID')  # Field name made lowercase.
    opcion_id = models.IntegerField(db_column='OPCION_ID')  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PROY_SISTEMA'
        # unique_together = (('id_proyecto', 'id_sistema'),)


class TbProySistMenu(models.Model):
    id_proyecto = models.ForeignKey(TbProySistema, models.DO_NOTHING,
                                    db_column='ID_PROYECTO', primary_key=True, related_name='proysist_idproyecto')  # Field name made lowercase.
    id_sistema = models.ForeignKey(TbProySistema, models.DO_NOTHING,
                                   db_column='ID_SISTEMA', primary_key=True, related_name='proysist_idsistema')  # Field name made lowercase.
    id_menu = models.AutoField(db_column='ID_MENU', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    nom_menu = models.CharField(db_column='NOM_MENU', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    des_menu = models.CharField(db_column='DES_MENU', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.
    padre_id = models.CharField(db_column='PADRE_ID', max_length=18, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_PROY_SIST_MENU'
        # unique_together = (('id_proyecto', 'id_sistema', 'id_menu'),)


class TbRolSistMenu(models.Model):
    id_proyecto = models.ForeignKey(TbProySistMenu, models.DO_NOTHING,
                                    db_column='ID_PROYECTO')  # Field name made lowercase.
    id_sistema = models.ForeignKey(TbProySistMenu, models.DO_NOTHING,
                                   db_column='ID_SISTEMA')  # Field name made lowercase.
    id_menu = models.ForeignKey(TbProySistMenu, models.DO_NOTHING, db_column='ID_MENU')  # Field name made lowercase.
    id_rol = models.ForeignKey(MaeRol, models.DO_NOTHING, db_column='ID_ROL')  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_ROL_SIST_MENU'
        # unique_together = (('id_proyecto', 'id_sistema', 'id_menu', 'id_rol'),)


class TbServicio(models.Model):
    servidor_id = models.IntegerField(db_column='SERVIDOR_ID')  # Field name made lowercase.
    servicio_id = models.AutoField(db_column='SERVICIO_ID')  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1)  # Field name made lowercase.
    nom_servicio = models.CharField(db_column='NOM_SERVICIO', max_length=18, blank=True,
                                    null=True)  # Field name made lowercase.
    puerto = models.CharField(db_column='PUERTO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=18, blank=True, null=True)  # Field name made lowercase.
    tipo_opcion_id1 = models.IntegerField(db_column='TIPO_OPCION_ID1')  # Field name made lowercase.
    opcion_id1 = models.IntegerField(db_column='OPCION_ID1')  # Field name made lowercase.
    tipo_opcion_id2 = models.IntegerField(db_column='TIPO_OPCION_ID2')  # Field name made lowercase.
    opcion_id2 = models.IntegerField(db_column='OPCION_ID2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_SERVICIO'
        # unique_together = (('servidor_id', 'servicio_id'),)


class TbServidor(models.Model):
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    servidor_id = models.CharField(db_column='SERVIDOR_ID', max_length=18)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    nom_servidor = models.CharField(db_column='NOM_SERVIDOR', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    direccion_ip = models.CharField(db_column='DIRECCION_IP', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    tipo_opcion_id1 = models.IntegerField(db_column='TIPO_OPCION_ID1')  # Field name made lowercase.
    opcion_id1 = models.IntegerField(db_column='OPCION_ID1')  # Field name made lowercase.
    tipo_opcion_id2 = models.IntegerField(db_column='TIPO_OPCION_ID2')  # Field name made lowercase.
    opcion_id2 = models.IntegerField(db_column='OPCION_ID2')  # Field name made lowercase.
    tipo_opcion_id3 = models.IntegerField(db_column='TIPO_OPCION_ID3')  # Field name made lowercase.
    opcion_id3 = models.IntegerField(db_column='OPCION_ID3')  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo_opcion_id4 = models.IntegerField(db_column='TIPO_OPCION_ID4')  # Field name made lowercase.
    opcion_id4 = models.IntegerField(db_column='OPCION_ID4')  # Field name made lowercase.
    observacion = models.CharField(db_column='OBSERVACION', max_length=250, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_SERVIDOR'


class TbUrlBloqueada(models.Model):
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.
    url_bloqueada_id = models.CharField(db_column='URL_BLOQUEADA_ID', max_length=18)  # Field name made lowercase.
    rango_inicio = models.CharField(db_column='RANGO_INICIO', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    rango_fin = models.CharField(db_column='RANGO_FIN', max_length=40, blank=True,
                                 null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='MOTIVO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_URL_BLOQUEADA'


class TbUsuarioConectado(models.Model):
    id_proyecto = models.IntegerField(db_column='ID_PROYECTO')  # Field name made lowercase.
    id_sistema = models.IntegerField(db_column='ID_SISTEMA')  # Field name made lowercase.
    id_menu = models.IntegerField(db_column='ID_MENU')  # Field name made lowercase.
    id_rol = models.IntegerField(db_column='ID_ROL')  # Field name made lowercase.
    id_permiso = models.IntegerField(db_column='ID_PERMISO')  # Field name made lowercase.
    id_usuario = models.IntegerField(db_column='ID_USUARIO')  # Field name made lowercase.
    fec_ingreso = models.DateTimeField(db_column='FEC_INGRESO', blank=True, null=True)  # Field name made lowercase.
    fec_salida = models.DateTimeField(db_column='FEC_SALIDA', blank=True, null=True)  # Field name made lowercase.
    direccion_ip = models.CharField(db_column='DIRECCION_IP', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    flag_activo = models.CharField(db_column='FLAG_ACTIVO', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    flag_eliminado = models.CharField(db_column='FLAG_ELIMINADO', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    usr_creacion = models.CharField(db_column='USR_CREACION', max_length=8, blank=True,
                                    null=True)  # Field name made lowercase.
    fec_creacion = models.DateTimeField(db_column='FEC_CREACION', blank=True, null=True)  # Field name made lowercase.
    usr_edicion = models.CharField(db_column='USR_EDICION', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    fec_edicion = models.DateTimeField(db_column='FEC_EDICION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_USUARIO_CONECTADO'
        # unique_together = (('id_proyecto', 'id_sistema', 'id_menu', 'id_rol', 'id_permiso', 'id_usuario'),)
