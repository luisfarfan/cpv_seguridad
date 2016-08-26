from seguridad.relaciones_models import *
from seguridad.maestros_models import *

# menu = ReMenu.objects.filter(padre_id__isnull=True).values()

# for hijo in menu:


obj = [{'id': 1, 'nombre': 'Luis Farfan', 'padre_id': None},
       {'id': 2, 'nombre': 'Ana Vega', 'padre_id': None},
       {'id': 3, 'nombre': 'Mayra Diaz', 'padre_id': None},
       {'id': 4, 'nombre': 'Eduardo Cabrera', 'padre_id': None},
       {'id': 5, 'nombre': 'Gustavo Peralta', 'padre_id': 1},
       {'id': 6, 'nombre': 'Omar Hernandez', 'padre_id': 1},
       {'id': 7, 'nombre': 'Gustavo Peralta', 'padre_id': 1},
       {'id': 8, 'nombre': 'Diego Paz', 'padre_id': 5},
       {'id': 9, 'nombre': 'Marco', 'padre_id': 5}]

nones = []
withids = []
for menus in obj:
    if menus.get('padre_id') == None:
        nones.append(menus)
    else:
        withids.append(menus)

list_nones = list(nones)
list_withids = list(withids)
print list_nones
print '**'*30

for k,v in enumerate(list_nones):
    for key,valor in enumerate(list_withids):
        if valor['padre_id'] == v['id']:
            list_nones[k]['items']=list_withids[key]

print list_nones

#print list_nones





