"""1.	La Municipalidad de Calera de Tango ha decidido promover la postura de chip a mascotas de la comuna, aplicando un descuento del 9% a los gatos y de 15% a 
los perros si usted es residente en la comuna, de lo contrario no habrá descuento. El costo de la intervención y por ende de la postura del chip tiene un valor de $10.000.
Se solicita que usted construya un programa en Python que permita obtener el valor a pagar, considerando sólo una mascota y si es residente o no de la comuna.
Valide que el ingreso del tipo de mascota sea sólo gato o perro."""


print("bienvenido a la Municipalidad de Calera")

residente=bool(input("¿Es usted recidente de la comuna ?  \nsi  \nno  "))
if(residente):
    print("Exelente usted a sido benefisiado con un descuento")
else:
    
    print("Usted debe cancelar el costo completo")
    

Mascota=int(input("¿ Usted tiene perro(1) o gato(2)"))

if(Mascota==1):
    print("oh que lindo un perro")
elif(Mascota==2):
    print("!!gatito¡¡")
else:
    print("Por favor elija una de las dos opciones")


Costofinal1=10000-10000*0.09
Costofinal2=10000-10000*0.15
Costofinal3=10000

if(residente) and (Mascota==2):
    print(f"El costo total del procedimiento, recibiendo el descuento de residente de la comuna es de:  {Costofinal1}\n ")
elif(residente) and (Mascota==1):
    print(f"El costo total del procedimiento, recibiendo el descuento de residente de la comuna es de:  {Costofinal2}\n ")
elif(residente) and (Mascota==1):
    print(f"El costo total procedimiento para ciudadano residente de otra comuna es de: {Costofinal3}\n ")
elif(residente) and (Mascota==2):
    print(f"El costo total procedimiento para ciudadano residente de otra comuna es de: {Costofinal3}\n ")
else:
    print("Ingrse info valida")

print("Gracias por ser parte de la campaña chipea a tu mascota")





