# Una clase con diferentes métodos según el tipo de trabajador (independiente, asalariado, etc.)

class CalculadoraDeImpuestos:
    def __init__(self, ingresos, tipo_trabajador):
        self.ingresos = ingresos
        self.tipo_trabajador = tipo_trabajador

    def calcular_impuesto(self):
        if self.tipo_trabajador == 'asalariado':
            return self.ingresos * 0.15  # 15% de impuesto
        elif self.tipo_trabajador == 'independiente':
            return self.ingresos * 0.20  # 20% de impuesto
        elif self.tipo_trabajador == 'pensionado':
            return self.ingresos * 0.10  # 10% de impuesto
        else:
            raise ValueError("Tipo de trabajador no reconocido")

    def mostrar_resultado(self):
        impuesto = self.calcular_impuesto()
        print(f"Tipo de trabajador: {self.tipo_trabajador}")
        print(f"Ingresos: ${self.ingresos:.2f}")
        print(f"Impuesto a pagar: ${impuesto:.2f}")
    
personal_asalariado = CalculadoraDeImpuestos(3000, 'asalariado')
personal_independiente = CalculadoraDeImpuestos(4000, 'independiente')
personal_pensionado = CalculadoraDeImpuestos(2000, 'pensionado')

personal_asalariado.mostrar_resultado()
personal_independiente.mostrar_resultado() 
personal_pensionado.mostrar_resultado()