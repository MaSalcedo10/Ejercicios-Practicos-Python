# crea una función que reciba una cadena y devuelva True si es un palíndromo, ignorando espacios y mayúsculas.
def palindromo():
    cadena = input("Introduce una cadena: ")
    # Eliminar espacios y convertir a minúsculas
    cadena_limpia = ''.join(cadena.split()).lower()
    # Comprobar si la cadena es igual a su reverso
    return cadena_limpia == cadena_limpia[::-1]

resultado = palindromo()
print("Es un palíndromo." if resultado else "No es un palíndromo.")