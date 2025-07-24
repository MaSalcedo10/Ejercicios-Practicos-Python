def numprimos(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

resultados = {}

for i in range(1, int(input("Ingrese un número: ")) + 1):
    if numprimos(i):
        resultados[i] = "Es primo"
    else:
        resultados[i] = "No es primo"

for numero, resultado in resultados.items():
    print(f"{numero}: {resultado}")

