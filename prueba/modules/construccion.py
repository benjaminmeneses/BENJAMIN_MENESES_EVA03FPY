

def const_menu(lista):
    for ind , opc in enumerate(lista):
        print(f'{ind +1}. {opc}')

def rec_resp():
    resp = input('Selecciona una opcion\n') 
    return resp 

def agregar():
    resp = input('ingresa los datos para agregar en formato\n Código: 380560, Nombre: Azul\n , Tipo : Acrílico ,Precio: 19990 \nStock: 133') 
    return resp     