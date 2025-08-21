class piedraPapeTijera:
    def __init__(self):
        self.choices = ['piedra', 'papel', 'tijera']

    def jugar(self, jugador1, jugador2):
        if jugador1 == jugador2:
            return "Empate"
        elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
             (jugador1 == 'papel' and jugador2 == 'piedra') or \
             (jugador1 == 'tijera' and jugador2 == 'papel'):
            return "Jugador 1 gana"
        else:
            return "Jugador 2 gana"

    def mostrar_opciones(self):
        return ", ".join(self.choices) 

    def validar_jugada(self, jugada):
        if jugada in self.choices:
            return True
        else:
            return False

    def jugar_con_input(self):
        jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
        while not self.validar_jugada(jugador1):
            print("Opción inválida. Inténtalo de nuevo.")
            jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()

        jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
        while not self.validar_jugada(jugador2):
            print("Opción inválida. Inténtalo de nuevo.")
            jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

        resultado = self.jugar(jugador1, jugador2)
        print(resultado)

if __name__ == "__main__":
    juego = piedraPapeTijera()
    juego.jugar_con_input()


