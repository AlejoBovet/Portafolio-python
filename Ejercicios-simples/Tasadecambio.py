"""2.	Genere un convertidor de:
•	Pesos chilenos a Grivna (UAH)
•	Pesos chilenos a Yen(JPY)
•	Pesos chilenos a Dólar hongkonés(HKD)
El usuario debe indicar la cantidad y el tipo de conversión a realizar, definiendo los valores de entrada, debiendo validar dicha entrada.
Por lo cual realice una aplicación Python que permita realizar lo solicitado."""


print("Bienvenido a casa de cambio duocuc")

Tipodemoneda=int(input("Indique a que tipo de moneda que quiere convertir \nGrivna(UAH)(1) \nYen(JPY)(2) \nDólar hongkonés(HKD)(3)\n "))

Cantidadpesoschilenos=int(input("Ingrese la cantidad a convertir"))

Yen=0.16*Cantidadpesoschilenos
Grivna=0.040*Cantidadpesoschilenos
HKD=0.011*Cantidadpesoschilenos


if(Tipodemoneda==1):
    print(f"La cantidad de ${Cantidadpesoschilenos} convertido en UAH es de {Grivna}")
elif(Tipodemoneda==2):
    print(f"La cantidad de ${Cantidadpesoschilenos} convertido en Yen es de {Yen}")
elif(Tipodemoneda==3):
    print(f"La cantidad de ${Cantidadpesoschilenos} convertido en HKD es de {HKD}")
else:
    print("ingrese un valor valido")

print("gracias por visitar casa de cambios duocuc")


