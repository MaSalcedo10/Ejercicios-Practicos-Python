# Implementa una función que devuelva los números primos hasta un número dado.

def es_primo(n):
    """
    Verifica si un número es primo.
    
    :param n: Número a verificar.
    :return: True si es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.") 
else:
    print(f"{numero} no es un número primo.")

