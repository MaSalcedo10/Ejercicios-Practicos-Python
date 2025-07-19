#Invierte las claves y valores de un diccionario (manejando si hay valores repetidos).

def diccionario_invertido(diccionario):
    """
    Invierte las claves y valores de un diccionario, manejando si hay valores repetidos.
    
    :param diccionario: Diccionario a invertir.
    :return: Diccionario invertido.
    """
    diccionario_invertido = {}
    
    for clave, valor in diccionario.items():
        if valor not in diccionario_invertido:
            diccionario_invertido[valor] = [clave]
        else:
            diccionario_invertido[valor].append(clave)
    
    return diccionario_invertido

midiccionario = {
    'a': 1, 'b': 2, 'c': 3,
    'd': 2, 'e': 1, 'f': 3}

resultado = diccionario_invertido(midiccionario)
print("Diccionario original:", midiccionario)
print("Diccionario invertido:", resultado)