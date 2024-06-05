# juego de pirdra papel y tijeras 

# Importar librias necesarias
import random
from os import system

# Variables
opcion = 0
RegistroPartidas = []


# saludo
print("Bienvenido al juego de piedra, papel o tijeras")

# limpiar pantalla
system("cls")

# menu de opciones
while(opcion!=3):
    print("\tMenu de opciones")
    print("\t1.Nueva partida")
    print("\t2. Historial de partidas")
    print("\t3. Salir")

    try:
        opcion=int(input("ingrese su opcion "))

        if(opcion==1):
            system("cls")
            print("\tPartida nueva")

            # Variables de la partida
            jugador1 = ""
            while(jugador1==""):
                jugador1=input("ingrese el nombre del jugador 1: ").lower()


            # empezar el juego
            jugador2 = "computadora"

            # eleccion de jugador 1
            eleccion = ""
            while eleccion not in ["piedra","papel","tijeras"]:
                eleccion = input("Ingrese su eleccion: ").lower()
                if eleccion not in ["piedra","papel","tijeras"]:
                    print("Eleccion invalida, intente de nuevo")

            # eleccion de jugador 2
            eleccion2 = random.choice(["piedra","papel","tijeras"])
            print(f"La computadora eligio: {eleccion2}")

            # comparacion de elecciones
            if eleccion == eleccion2:
                print("Empate")
                resultado = "Empate"
            elif eleccion == "piedra" and eleccion2 == "tijeras":
                print(f"{jugador1} gana")
                resultado = f"{jugador1} gana"
            elif eleccion == "papel" and eleccion2 == "piedra":
                print(f"{jugador1} gana")
                resultado = f"{jugador1} gana"
            elif eleccion == "tijeras" and eleccion2 == "papel":
                print(f"{jugador1} gana")
                resultado = f"{jugador1} gana"
            else:
                print("Computadora gana")
                resultado = "Computadora gana"

            # Guardar partida
            RegistroPartidas.append({
                "jugador1": jugador1,
                "jugador2": jugador2,
                "eleccion1": eleccion,
                "eleccion2": eleccion2,
                "resultado": resultado
            })

        elif(opcion==2):
            system("cls")
            print("\tHistorial de partidas")

            # Recorrer el historial de partidas
            for partida in RegistroPartidas:
                print(f"Jugador 1: {partida['jugador1']}")
                print(f"Jugador 2: {partida['jugador2']}")
                print(f"Jugador 1 eligio: {partida['eleccion1']}")
                print(f"Jugador 2 eligio: {partida['eleccion2']}")
                print(f"Resultado: {partida['resultado']}")
                print("")
            input("enter para seguir")

        elif(opcion==3):
            system("cls")
            print("\tSalir, gracias por jugar")
        
        else:
            print("opcion invalida")

    except:
        print("solo puede ingresar un nro")