import threading
import time
from module import contar_palabras

#creamos el menu
print("Bienvenido a mi juego de cuantas palabras puedes escribir en un minuto")
print("Instrucciones: Escribe la mayor cantidad de palabras en un minuto")
print("Presiona Enter para empezar")

RegistroPalabras = []
tiempo = [10]  # usamos una lista para que el hilo del temporizador pueda modificarla

def countdown():
    while tiempo[0] > 0:
        time.sleep(1)
        tiempo[0] -= 1

threading.Thread(target=countdown).start()

while tiempo[0] > 0:
    palabra = input("ingresa una palabra: ")
    RegistroPalabras.append(palabra)
    contar_palabras(RegistroPalabras)

print("Tiempo terminado")
input("Presiona para cerrar")

