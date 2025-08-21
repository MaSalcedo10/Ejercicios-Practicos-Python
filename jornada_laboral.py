hora_ingreso = input("Ingrese la hora de ingreso (HH:MM): ")
hora_salida = input("Ingrese la hora de salida (HH:MM): ")

hora_ingreso = hora_ingreso.split(':')
hora_salida = hora_salida.split(':')

hora_ingreso = int(hora_ingreso[0]) * 60 + int(hora_ingreso[1])
hora_salida = int(hora_salida[0]) * 60 + int(hora_salida[1])

def calcular_jornada(hora_ingreso, hora_salida):
    if hora_salida < hora_ingreso:
        return "Error: La hora de salida no puede ser anterior a la hora de ingreso."
    jornada = hora_salida - hora_ingreso
    horas = jornada // 60
    minutos = jornada % 60
    return f"El total de tiempo trabajo fue de: {horas} horas y {minutos} minutos."

def horas_extras(hora_ingreso, hora_salida):
    jornada_normal = 8 * 60  # 8 horas en minutos
    if hora_salida - hora_ingreso > jornada_normal:
        return (hora_salida - hora_ingreso) - jornada_normal
    return 0

print(calcular_jornada(hora_ingreso, hora_salida))

if horas_extras(hora_ingreso, hora_salida) > 0:
    horas_extra = horas_extras(hora_ingreso, hora_salida)
    horas = horas_extra // 60
    minutos = horas_extra % 60
    print(f"Horas extras trabajadas: {horas} horas y {minutos} minutos.")
    
