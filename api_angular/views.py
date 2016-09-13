from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from seguridad.helpers import json_serial
from seguridad.db_views import ViewPermisosMenuChild
from django.utils.text import slugify

def menu(request):
    menustring = '<div class="sidebar-content"><div class="sidebar-category sidebar-category-visible"><div class="category-content no-padding"><ul class="navigation navigation-main navigation-accordion"><li class="navigation-header"><span>Menu Principal</span><i class="icon-menu" title="Main pages"></i></li>';
    menu = []
    if(request.method == 'GET'):
        id = request.GET.get('id_usuario', False)
        menu = get_session(id)
        for k,v in enumerate(menu):
            menustring+='<li><a><i class="icon-home4"></i><span>'+v['TITULO']+'</span></a>'
            if 'hijos' in v:
                menustring+='<ul>'
                for kk,vv in enumerate(v['hijos']):
                    menustring+='<li><a routerLink="/'+slugify(vv['TITULO'])+'" routerLinkActive="active">'+vv['TITULO']+'</a></li>'
                menustring+='</ul></li>'
            else:
                menustring+='</li>'

    menustring+='</ul></div></div></div>'
    return HttpResponse(json.dumps({'menu':menustring}), content_type='application/json')


def routes(request):
    if(request.method == 'GET'):
        id = request.GET.get('id_usuario', False)
        menu = menu_parent_child(id)
        route = []
        for k in menu:
            if k['PADRE_ID']!=None:
                route.append(slugify(k['TITULO']))

    return HttpResponse(json.dumps(route), content_type='application/json')


def get_routes(id):
    menu = menu_parent_child(id)
    route = []
    for k in menu:
        if k['PADRE_ID']!=None:
            route.append(slugify(k['TITULO']))

    return route


def get_session(id):
    menu=set_permissions_to_menu_child(permissions(id), menu_parent_child(id))
    
    return menu
    #return HttpResponse(json.dumps(menu, default=json_serial), content_type='application/json')


def permissions(id):
    permisos = list(ViewPermisosMenuChild.objects.filter(id_usuario=id).values(
        'cod_permiso', 'nom_permiso', 'des_rol', 'id_menu'))

    return permisos


def menu_parent_child(id):
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute('exec getMenubyUser %s', [id])
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))

    return menu


def set_permissions_to_menu_child(permissions, menu):
    padres = []
    hijos = []
    for k, v in enumerate(menu):
        if menu[k]['PADRE_ID'] == None:
            padres.append(menu[k])
        else:
            hijos.append(menu[k])

    for k, v in enumerate(hijos):
        permisos = []
        for kk, vv in enumerate(permissions):
            if vv['id_menu'] == v['ID_MENU']:
                permisos.append(dict(permissions[kk]))
                hijos[k]['permisos'] = permisos

    for k, v in enumerate(padres):
        listadict = []
        for kk, vv in enumerate(hijos):
            if hijos[kk]['PADRE_ID'] == padres[k]['ID_MENU']:
                listadict.append(dict(hijos[kk]))
                padres[k]['hijos'] = listadict

    return padres
