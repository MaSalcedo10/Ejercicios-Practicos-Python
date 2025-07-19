def mi_decorador(func):
    def envolvedora():
        print("Antes de la ejecución de la función")
        func()
        print("Después de la ejecución de la función")
    return envolvedora

@mi_decorador
def saludar():
    print("Hola, mundo!")

saludar()