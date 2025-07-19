# FizzBuzz clásico: imprime del 1 al 100, 
# pero sustituye múltiplos de 3 con “Fizz”, 
# de 5 con “Buzz”, y de ambos con “FizzBuzz”.

def fizz_buzz_clasico():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
print(fizz_buzz_clasico())
