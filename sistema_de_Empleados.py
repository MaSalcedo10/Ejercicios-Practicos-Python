#Crea clases Empleado, Gerente, y Desarrollador, con herencia y polimorfismo.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        return f"Gerente: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}"

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        return f"Desarrollador: {self.nombre}, Salario: {self.salario}, Lenguaje: {self.lenguaje}"

empleados = [
    Empleado("Ana", 1000),
    Gerente("Luis", 2000, "Ventas"),
    Desarrollador("Marta", 1500, "Python")
]

for emp in empleados:
    print(emp.mostrar_informacion())