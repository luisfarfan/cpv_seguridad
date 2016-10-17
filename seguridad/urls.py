from views import *


router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'sistemas', SistemaViewSet)
router.register(r'permisos', PermisosViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'proyectos_sistemas', ProyectoSistemaViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'menu_permisos', MenuPermisosViewSet)
router.register(r'menu_permisos_rol', MenuPermisosRolViewSet)
router.register(r'menu_permisos_rol_usuario', MenuPermisosRolUsuarioViewSet)
router.register(r'proyectos-by-sistemas', ProyectosbySistemaViewSet)
