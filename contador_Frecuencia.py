#dado un string, cuenta cuántas veces aparece cada letra (sin contar espacios ni signos de puntuación).

def contador_frecuencia(texto):
    # Convertir el texto a minúsculas y eliminar espacios y signos de puntuación
    texto = ''.join(c.lower() for c in texto if c.isalpha())
    
    # Crear un diccionario para contar la frecuencia de cada letra
    frecuencia = {}
    
    for letra in texto:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
            
    return frecuencia

resultado = contador_frecuencia("Hola, mundo! ¿Cómo estás?")
print(resultado)