#Juega de impar o par.

def par_o_impar(numero):
    if numero % 2 == 0:
        return "Es un numero Par"
    else:
        return "Es un numero Impar"
    

numero = 0
print( "Juguemos al juego de par o impar ")
while numero < 1 or numero > 100:
    numero = int(input("Ingresa un numero del 1 al 100: "))
    if numero >= 1 and numero <= 100:
        print(par_o_impar(numero))
        break
    print("El numero no esta en el rango")
