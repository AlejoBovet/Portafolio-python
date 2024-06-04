# Contador de palabras 

def contar_palabras(texto):
    palabras = texto.split(" ")
    print(f"Me has demostrado tu pensamiento en {len(palabras)} palabras.")

print("Contador de palabras")
texto = input("En que estas pensando: \n")
contar_palabras(texto)
