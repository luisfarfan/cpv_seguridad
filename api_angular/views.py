from django.http import HttpResponse
import json
from seguridad.db_views import ViewPermisosMenuChild
from django.utils.text import slugify


def menu(request):
    if (request.method == 'GET'):
        #id = request.GET.get('id_usuario', False)
        menu = recursive_menu_tree()

    return HttpResponse(json.dumps(menu), content_type='application/json')

def menu_tree(request):
    tree = []


def recursive_menu_session():
    menu = get_session(1)
    clone = menu
    resultado = []
    for k, v in enumerate(clone):
        for kk, vv in enumerate(menu):
            if clone[k]['PADRE_ID'] == menu[kk]['ID_MENU']:
                menu[kk]['childs'].append(dict(clone[k]))

    for k, v in enumerate(menu):
        if v['PADRE_ID'] is None:
            resultado.append(v)

    return resultado

def recursive_menu_tree():
    menu = get_session(1)
    menures = []
    for k, v in enumerate(menu):
        del menu[k]['sigla_proy']
        del menu[k]['ID_PROYECTO']
        del menu[k]['DES_SIST']
        del menu[k]['ID_SISTEMA']
        if 'permisos' in menu[k]:
            del menu[k]['permisos']
        menures.append(
            {'id': menu[k]['ID_MENU'],
             'name':menu[k]['TITULO'],
             'children':[],
             'padre_id':menu[k]['PADRE_ID'],
             'slug':slugify(menu[k]['TITULO'])
             })


    clone = menures
    resultado = []
    for k, v in enumerate(clone):
        for kk, vv in enumerate(menures):
            if clone[k]['padre_id'] == menures[kk]['id']:
                menures[kk]['children'].append(dict(clone[k]))

    for k, v in enumerate(menures):
        if v['padre_id'] is None:
            resultado.append(v)

    return resultado

def menu_singapp(request):
    menustring = '<ul class="sidebar-nav">'
    menu = []
    if (request.method == 'GET'):
        id = request.GET.get('id_usuario', False)
        menu = get_session(id)
        for k, v in enumerate(menu):
            menustring += '<li><a class="collapsed" data-target="#sidebar-%s" data-toggle="collapse" data-parent="#sidebar"><span class="icon"><i class="fa fa-desktop"></i></span>%s<i class="toggle fa fa-angle-down"></i></a>' % (
                slugify(v['TITULO']), v['TITULO'])
            if 'hijos' in v:
                menustring += '<ul class="collapse" id="sidebar-%s">' % (slugify(v['TITULO']))
                for kk, vv in enumerate(v['hijos']):
                    menustring += '<li><a routerLink="' + slugify(vv['TITULO']) + '">' + vv['TITULO'] + '</a></li>'
                menustring += '<li><a routerLink="reportes">REPORTES</a></li>'
                menustring += '</ul></li>'
            else:
                menustring += '</li>'
    menustring += '</ul>'
    return HttpResponse(json.dumps({'menu': menustring, 'data': menu}), content_type='application/json')


def routes(request):
    if (request.method == 'GET'):
        id = request.GET.get('id_usuario', False)
        menu = menu_parent_child(id)
        route = []
        for k in menu:
            if k['PADRE_ID'] != None:
                route.append(slugify(k['TITULO']))

    return HttpResponse(json.dumps(route), content_type='application/json')


def get_routes(id):
    menu = menu_parent_child(id)
    route = []
    for k in menu:
        if k['PADRE_ID'] != None:
            route.append(slugify(k['TITULO']))

    return route


def get_session(id):
    menu = set_permissions_to_menu_child(permissions(id), menu_parent_child(id))

    return menu
    # return HttpResponse(json.dumps(menu, default=json_serial), content_type='application/json')


def permissions(id):
    permisos = list(ViewPermisosMenuChild.objects.filter(id_usuario=id).values(
        'cod_permiso', 'nom_permiso', 'des_rol', 'id_menu'))

    return permisos


def menu_parent_child(id):
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute('exec getMenubyUser %s', [str(id)])
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

    for k, v in enumerate(menu):
        permisos = []
        menu[k]['childs'] = []
        for kk, vv in enumerate(permissions):
            if vv['id_menu'] == v['ID_MENU']:
                permisos.append(dict(permissions[kk]))
                menu[k]['permisos'] = permisos

    return menu