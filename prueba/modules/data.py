from pathlib import Path
import json
import csv
home = Path(__file__).parent.parent
ruta_j = Path(home/'archivo.json')
ruta_c = Path(home/'mandarina.csv')

menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas',
         'Salir']

data = {'Código': 380560,
        'Nombre': 'Azul',
        'Tipo' : 'Acrílico',
        'Precio': 19990,
        'Stock': 133}


def verif_ex(ruta_j):
    while True:
        if not ruta_j.exists():
            ruta_j.touch()
        else:
            return ruta_j

def verf_esp(ruta_j):
    if ruta_j.stat().st_size == 0:
        with open(ruta_j, 'w') as stream:
            archivo_j = [] 
            json.dump(archivo_j, stream)


def mostrar_j(ruta_j):
    with open(ruta_j, 'r') as stream:
        json.load(stream) 


#def exportar():
    #with open(ruta_j , 'r') as stream:
     #   for elemt, opt in ruta_j:


