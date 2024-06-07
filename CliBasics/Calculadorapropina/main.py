#Calculadora 
#importaciones
from os import system 
from modules import conversor,propina,descuento

#variables globales
opcion=0
montofinal=0

print('Calculadora de propina')
print('')

#Menu de opciones
system("cls")
while(opcion!=2):

    print("\t Menu de opciones ")
    print("\t1.  Calcular propina")
    print("\t2.  Salir")

    try:
        opcion=int(input("ingrese su opcion "))

        #Calculo de propina
        if(opcion==1):
            system("cls")
            print("\t Calculo de propina")
            #variable local
            cantidad0=0
            opcion2=0
            
            #submenu1
            system("cls")
            while(opcion2!=4):
                print("\t Menu de opciones propina ")
                print("\t1.  Conversor divisa")
                print("\t2.  Calcular propina")
                print("\t3.  Descuento")
                print("\t4.  Salir")

                try:
                    opcion2=int(input("ingrese su opcion "))

                    #Conversor de divisa
                    if(opcion2==1):
                        system("cls")
                        print("\t Conversor de divisa")
                        cantidad = int(input('Ingrese la cantidad a convertir: '))
                        tipo_moneda = input('Ingrese el tipo de moneda a convertir: ').lower()
                        cantidad0 = conversor(tipo_moneda,cantidad)
                        print(f'La cantidad convertida es: {cantidad0} en {tipo_moneda}')

                    #Calculo de propina
                    elif(opcion2==2):
                        system("cls")
                        print("\t Calculo de propina")
                        cantidad = int(input('Ingrese la cantidad a calcular: '))
                        porcentaje = int(input('Ingrese el número correspondiente al tipo de propina: 1 para 10%, 2 para 15%, 3 para 30%: '))
                        montofinal = propina(cantidad,porcentaje)
                        print(f'El monto de la propina es: {montofinal}')
                    
                    #Descuento
                    elif(opcion2==3):
                        system("cls")
                        print("\t Descuento")
                        cantidad = int(input('Ingrese la cantidad a calcular: '))
                        tipo_cliente = input('Ingrese el tipo de cliente entre (bronce,plata y oro): ').lower()
                        montofinal = descuento(cantidad,tipo_cliente)
                        print(f'El monto con descuento es: {montofinal}')

                except:
                    print('Ingrese un numero valido')
        elif(opcion==2):
            print('Gracias por usar la calculadora de propina')
        else:
            print('Ingrese un numero valido')

    except:
        print('Ingrese un numero valido')