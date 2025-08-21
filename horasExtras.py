jornadaLaboral = 44  # horas por semana

def calcularHorasExtras(horasTrabajadas):
    """
    Calcula las horas extras trabajadas en una semana.
    
    :param horasTrabajadas: Número total de horas trabajadas en la semana.
    :return: Número de horas extras trabajadas.
    """
    if horasTrabajadas <= jornadaLaboral:
        return 0
    else:
        return horasTrabajadas - jornadaLaboral

def calcularPagoHorasExtras(horasTrabajadas, tarifaHora):
    """
    Calcula el pago por horas extras trabajadas.
    
    :param horasTrabajadas: Número total de horas trabajadas en la semana.
    :param tarifaHora: Tarifa por hora normal.
    :return: Pago total por horas extras.
    """
    horasExtras = calcularHorasExtras(horasTrabajadas)
    if horasExtras > 0:
        tarifaHoraExtra = tarifaHora * 1.5  # Tarifa por hora extra
        return horasExtras * tarifaHoraExtra
    else:
        return 0

def main():
    horasTrabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
    tarifaHora = float(input("Ingrese la tarifa por hora normal: "))
    
    horasExtras = calcularHorasExtras(horasTrabajadas)
    pagoExtras = calcularPagoHorasExtras(horasTrabajadas, tarifaHora)
    
    print(f"Horas extras trabajadas: {horasExtras}")
    print(f"Pago total por horas extras: ${pagoExtras:.2f}")

if __name__ == "__main__":
    main()