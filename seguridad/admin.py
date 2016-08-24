from django.contrib import admin
from maestros_models import *
from relaciones_models import *

# Tablas maestras :
admin.site.register(MaeUsuario)
admin.site.register(MaeProyecto)
admin.site.register(MaeSistema)
admin.site.register(MaePermiso)
admin.site.register(MaeRol)

# Tablas Relacionadas

admin.site.register(ReProyectoSistema)
admin.site.register(ReMenu)
admin.site.register(ReMenuPermisosRol)
admin.site.register(ReMenuPermisos)
admin.site.register(ReMenuPermisosRolUsuario)
#admin.site.register(ReMenuRol)