#Escribe una función que retorne los elementos comunes entre dos listas.

def interseccion_listas(lista1, lista2):
    """
    Retorna una lista con los elementos comunes entre lista1 y lista2.
    
    :param lista1: Primera lista de elementos.
    :param lista2: Segunda lista de elementos.
    :return: Lista con los elementos comunes.
    """
    return list(set(lista1) & set(lista2))

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]    
resultados = interseccion_listas(lista1, lista2)
print("Elementos comunes:", resultados)