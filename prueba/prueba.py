from pathlib import Path
import json
import csv
from modules.construccion import const_menu, rec_resp, agregar
from modules.data import menup, verif_ex, verf_esp, mostrar_j, ruta_j, ruta_c , data


while True:
    const_menu(menup)
    ans = rec_resp()
    if ans == '1':
        basededatos = mostrar_j(ruta_j)
        if len(basededatos) == 0:
            print('Error: EL archivo esta vacio')
        else:
            print(mostrar_j(ruta_j)) 

    elif ans == '2':
        pass

    elif ans == '3':
        while True:
            print('ingresa los datos para agregar, en formato\nCódigo: 380560, Nombre:Azul\nTipo : Acrílico, Precio: 19990 \nStock: 133\n')
            codig = int(input('codigo:'))
            nom = input('nombre:')
            tipo = input('tipo:')
            precio = int(input('precio:'))
            stock = int(input('stock:\n'))
            respu = input(f'codigo: {codig}\nnombre: {nom}\ntipo: {tipo}\nprecio: {precio}\n stock: {stock}\n¿Esta bien?\ns/n si/no\n')
            if respu == 's' or respu== 'si':
                continue
            elif respu == 'n' or 'no':
                pass
    elif ans == '4':
        pass
    elif ans == '5':
        pass
    elif ans == '6':
        exit('Adios!')
    else:
        print('Error: Opcion no valida')