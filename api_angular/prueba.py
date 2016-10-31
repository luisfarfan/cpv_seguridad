from api_angular.views import *


def getmenu():
    menu = get_session(1)
    for k, v in enumerate(menu):
        for kk, vv in enumerate(menu):
            if menu[k]['PADRE_ID'] == menu[kk]['ID_MENU']:
                menu[kk]['childs'] = menu[k]
    return menu
