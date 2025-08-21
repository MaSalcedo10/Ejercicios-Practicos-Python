class jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def __str__(self):
        return f"Jugador: {self.nombre}, Edad: {self.edad}"

# Ejemplo de uso
if __name__ == "__main__":
    jugador1 = jugador("Alice", 25)
    print(jugador1.saludar())
    print(f"¿Es mayor de edad? {'Sí' if jugador1.es_mayor_de_edad() else 'No'}")
    print(jugador1)
    
    jugador2 = jugador("Bob", 17)
    print(jugador2.saludar())
    print(f"¿Es mayor de edad? {'Sí' if jugador2.es_mayor_de_edad() else 'No'}")
    print(jugador2)    