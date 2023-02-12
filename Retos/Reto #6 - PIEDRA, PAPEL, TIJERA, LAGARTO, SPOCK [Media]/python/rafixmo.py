# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
# 12/03/23
#
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#
# Solución al reto #6
# Autor: Rafixmo


import ast, emoji

juego = {
    ":moai:": [":lizard:", ":scissors:"], # "piedra"
    ":page_facing_up:": [":moai:", ":vulcan_salute:"], # "papel"
    ":scissors:": [":page_facing_up:", ":lizard:"], # "tijeras"
    ":lizard:": [":vulcan_salute:", ":page_facing_up:"], # "largarto"
    ":vulcan_salute:": [":scissors:", ":moai:"] # "spock"
}


def calcula_solucion_jugada (jugada):

    if jugada[1] == jugada[0]:
        return 0 # empate
    elif jugada[1] in juego.get(jugada[0]): 
        return 1 # gana
    else:
        return -1 # pierde


def leer_jugadas(entrada):

    return ast.literal_eval(entrada)



def jugar_con_teclado():

    print("Introduzca la jugada: ")
    jugar(input())


def jugar_con_fichero():
    txt_file = open("jugadas.txt", "r", encoding="utf-8")

    for line in txt_file.readlines():
        print(line)
        jugar(line)


def jugar(linea_jugada):

    jugadas = leer_jugadas(emoji.demojize(linea_jugada))

    resultado = 0
    for jugada in jugadas:
        resultado += calcula_solucion_jugada (jugada)

    if resultado == 0:
        print("Empate")
    elif resultado > 0:
        print("Gana Player1.")
    else:
        print("Gana Player2.")


print("Bienvenido al juego " + chr(int("1F5FF", 16)) + chr(int("1F4C4", 16)) +
       chr(int("2702", 16)) + chr(int("1F98E", 16)) + chr(int("1F596", 16)) + ":")

print("Opciones:")
print("1. Introducir una jugada por teclado")
print("2. Leer jugadas de fichero")

opcion= input()

if opcion == "1":
    jugar_con_teclado()
elif opcion == "2":
    jugar_con_fichero()
else:
    print("Opción incorrecta.")


# contenido fichero jugadas.txt
"""
[("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
[("🦎","🖖"), ("✂️","🦎"), ("📄","📄")]
[("🗿","📄"), ("🖖","📄"), ("✂️","📄")]
"""