# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-30 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewPermisosMenuChild',
            fields=[
                ('id_permisosusuario', models.IntegerField(db_column='ID_PERMISOSUSUARIO', primary_key=True, serialize=False)),
                ('id_menu', models.IntegerField(db_column='ID_MENU')),
                ('cod_permiso', models.CharField(db_column='COD_PERMISO', max_length=4)),
                ('nom_permiso', models.CharField(db_column='NOM_PERMISO', max_length=15)),
                ('des_rol', models.CharField(db_column='DES_ROL', max_length=50)),
                ('id_usuario', models.IntegerField(db_column='ID_USUARIO')),
            ],
            options={
                'db_table': 'permisos_menu_child',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaePermiso',
            fields=[
                ('id_permiso', models.AutoField(db_column='ID_PERMISO', primary_key=True, serialize=False)),
                ('des_permiso', models.CharField(blank=True, db_column='DES_PERMISO', max_length=100, null=True)),
                ('cod_permiso', models.CharField(blank=True, db_column='COD_PERMISO', max_length=4, null=True)),
                ('nom_permiso', models.CharField(blank=True, db_column='NOM_PERMISO', max_length=50, null=True)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
            ],
            options={
                'db_table': 'MAE_PERMISO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaeProyecto',
            fields=[
                ('id_proyecto', models.AutoField(db_column='ID_PROYECTO', primary_key=True, serialize=False)),
                ('sigla_proy', models.CharField(blank=True, db_column='SIGLA_PROY', max_length=20, null=True)),
                ('anio_proy', models.CharField(blank=True, db_column='ANIO_PROY', max_length=4, null=True)),
                ('des_proy', models.CharField(blank=True, db_column='DES_PROY', max_length=255, null=True)),
                ('tipo_proy', models.CharField(blank=True, db_column='TIPO_PROY', max_length=1, null=True)),
                ('fec_inicio', models.DateTimeField(blank=True, db_column='FEC_INICIO', null=True)),
                ('fec_final', models.DateTimeField(blank=True, db_column='FEC_FINAL', null=True)),
                ('observacion', models.CharField(blank=True, db_column='OBSERVACION', max_length=250, null=True)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('cod_meta', models.CharField(blank=True, db_column='COD_META', max_length=8, null=True)),
            ],
            options={
                'db_table': 'MAE_PROYECTO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaeRol',
            fields=[
                ('id_rol', models.AutoField(db_column='ID_ROL', primary_key=True, serialize=False)),
                ('des_rol', models.CharField(blank=True, db_column='DES_ROL', max_length=100, null=True)),
                ('nom_rol', models.CharField(blank=True, db_column='NOM_ROL', max_length=50, null=True)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
            ],
            options={
                'db_table': 'MAE_ROL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaeSistema',
            fields=[
                ('id_sistema', models.AutoField(db_column='ID_SISTEMA', primary_key=True, serialize=False)),
                ('des_sist', models.CharField(blank=True, db_column='DES_SIST', max_length=100, null=True)),
                ('nom_sist', models.CharField(blank=True, db_column='NOM_SIST', max_length=50, null=True)),
                ('codigo_sist', models.CharField(blank=True, db_column='CODIGO_SISTEMA', max_length=20, null=True)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
            ],
            options={
                'db_table': 'MAE_SISTEMA',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaeTipoUsuario',
            fields=[
                ('id_tipousuario', models.AutoField(db_column='ID_TIPOUSUARIO', primary_key=True, serialize=False)),
                ('nombre_tipousuario', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion_tipousuario', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'TIPO_USUARIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaeUsuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='ID_USUARIO', primary_key=True, serialize=False)),
                ('dni', models.CharField(db_column='DNI', max_length=8)),
                ('ape_pat_per', models.CharField(blank=True, db_column='APE_PAT_PER', max_length=35, null=True)),
                ('ape_mat_per', models.CharField(blank=True, db_column='APE_MAT_PER', max_length=35, null=True)),
                ('nom_emp_per', models.CharField(blank=True, db_column='NOM_EMP_PER', max_length=35, null=True)),
                ('fecha_contrato_inicio', models.DateField(blank=True, null=True)),
                ('fecha_contrato_fin', models.DateField(blank=True, null=True)),
                ('fecha_contrato_fin_extended', models.DateField(blank=True, null=True)),
                ('fec_nac_per', models.DateField(blank=True, db_column='FEC_NAC_PER', null=True)),
                ('email_insti', models.CharField(blank=True, db_column='EMAIL_INSTI', max_length=50, null=True)),
                ('email_personal', models.CharField(blank=True, db_column='EMAIL_PERSONAL', max_length=50, null=True)),
                ('sex_emp_per', models.CharField(blank=True, db_column='SEX_EMP_PER', max_length=1, null=True)),
                ('nom_completo', models.CharField(blank=True, db_column='NOMBRE_COMPLETO', max_length=250, null=True)),
                ('usuario', models.CharField(blank=True, db_column='USUARIO', max_length=20, null=True)),
                ('clave', models.CharField(blank=True, db_column='CLAVE', max_length=20, null=True)),
                ('id_tipousuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.MaeTipoUsuario')),
            ],
            options={
                'db_table': 'USUARIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReMenu',
            fields=[
                ('id_menu', models.AutoField(db_column='ID_MENU', primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, db_column='TITULO', max_length=50, null=True)),
                ('nom_menu', models.CharField(blank=True, db_column='NOM_MENU', max_length=100, null=True)),
                ('des_menu', models.TextField(blank=True, db_column='DES_MENU')),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('url', models.CharField(blank=True, db_column='URL', max_length=100, null=True)),
                ('slug', models.CharField(blank=True, db_column='slug', max_length=100, null=True)),
                ('img', models.CharField(blank=True, db_column='IMG', max_length=255, null=True)),
            ],
            options={
                'db_table': 'TB_MENU',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReMenuPermisos',
            fields=[
                ('id_menupermisos', models.AutoField(db_column='ID_MENUPERMISOS', primary_key=True, serialize=False)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('id_menu', models.ForeignKey(db_column='ID_MENU', on_delete=django.db.models.deletion.CASCADE, to='seguridad.ReMenu')),
                ('id_permiso', models.ForeignKey(db_column='ID_PERMISO', on_delete=django.db.models.deletion.CASCADE, to='seguridad.MaePermiso')),
            ],
            options={
                'db_table': 'TB_PERMISOS_MENU',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReMenuPermisosRol',
            fields=[
                ('id_menupermisosrol', models.AutoField(db_column='ID_MENUPERMISOSROL', primary_key=True, serialize=False)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('id_menupermisos', models.ForeignKey(db_column='ID_MENUPERMISOS', on_delete=django.db.models.deletion.CASCADE, related_name='menupermisos', to='seguridad.ReMenuPermisos')),
                ('id_rol', models.ForeignKey(db_column='ID_ROL', on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='seguridad.MaeRol')),
            ],
            options={
                'db_table': 'TB_MENU_PERMISOS_ROL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReMenuPermisosRolUsuario',
            fields=[
                ('id_permisosusuario', models.AutoField(db_column='ID_PERMISOSUSUARIO', primary_key=True, serialize=False)),
                ('flag_activo', models.CharField(blank=True, db_column='FLAG_ACTIVO', max_length=1, null=True)),
                ('flag_eliminado', models.CharField(blank=True, db_column='FLAG_ELIMINADO', max_length=1, null=True)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('id_menupermisosrol', models.ForeignKey(db_column='ID_MENUPERMISOSROL', on_delete=django.db.models.deletion.CASCADE, to='seguridad.ReMenuPermisosRol')),
                ('id_usuario', models.ForeignKey(db_column='ID_USUARIO', on_delete=django.db.models.deletion.CASCADE, to='seguridad.MaeUsuario')),
            ],
            options={
                'db_table': 'TB_MENU_PERMISOS_ROL_USUARIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReProyectoSistema',
            fields=[
                ('id_proyectosistema', models.AutoField(db_column='ID_PROYECTOSISTEMA', primary_key=True, serialize=False)),
                ('usr_creacion', models.CharField(blank=True, db_column='USR_CREACION', max_length=8, null=True)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True, db_column='FEC_CREACION')),
                ('usr_edicion', models.CharField(blank=True, db_column='USR_EDICION', max_length=8, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, db_column='FEC_EDICION', null=True)),
                ('titulo_sistema_padre', models.CharField(blank=True, db_column='TITULO_SISTEMA_PADRE', max_length=50, null=True)),
                ('id_proyecto', models.ForeignKey(db_column='ID_PROYECTO', on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='seguridad.MaeProyecto')),
                ('id_sistema', models.ForeignKey(db_column='ID_SISTEMA', on_delete=django.db.models.deletion.CASCADE, related_name='sistemas', to='seguridad.MaeSistema')),
            ],
            options={
                'db_table': 'TB_PROYECTO_SISTEMA',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='remenu',
            name='id_proyectosistema',
            field=models.ForeignKey(db_column='ID_PROYECTOSISTEMA', on_delete=django.db.models.deletion.CASCADE, to='seguridad.ReProyectoSistema'),
        ),
        migrations.AddField(
            model_name='remenu',
            name='padre_id',
            field=models.ForeignKey(blank=True, db_column='PADRE_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='seguridad.ReMenu'),
        ),
        migrations.AddField(
            model_name='maerol',
            name='menupermisos',
            field=models.ManyToManyField(through='seguridad.ReMenuPermisosRol', to='seguridad.ReMenuPermisos'),
        ),
        migrations.AddField(
            model_name='maeproyecto',
            name='sistemas',
            field=models.ManyToManyField(through='seguridad.ReProyectoSistema', to='seguridad.MaeSistema'),
        ),
        migrations.AlterUniqueTogether(
            name='maepermiso',
            unique_together=set([('cod_permiso',)]),
        ),
        migrations.AlterUniqueTogether(
            name='reproyectosistema',
            unique_together=set([('id_proyecto', 'id_sistema')]),
        ),
        migrations.AlterUniqueTogether(
            name='remenupermisosrolusuario',
            unique_together=set([('id_menupermisosrol', 'id_usuario')]),
        ),
        migrations.AlterUniqueTogether(
            name='remenupermisosrol',
            unique_together=set([('id_rol', 'id_menupermisos')]),
        ),
        migrations.AlterUniqueTogether(
            name='remenupermisos',
            unique_together=set([('id_menu', 'id_permiso')]),
        ),
    ]
