# Lista de informacion de biografia

#importaciones
from os import system 
import random 
import re


#funciones


#Menu de opciones

opcion=0
registros=[]

system("cls")
while(opcion!=3):

    print("\t Menu de informacion de biografia ")
    print("\t1.  Registro de biografia")
    print("\t2.  imprimir biografia")
    print("\t3.  Salir")

    try:
        opcion=int(input("ingrese su opcion "))

    #Registro de biografia

        if (opcion==1):
            system("cls")
            print("\t Registro de biografia")

        
            codigo=random.randint(1,9999)
                

            nombre=""
            while(nombre==""):
                nombre=input("ingrese el nombre: ").lower()
                
            apellido=""
            while(apellido==""):
                apellido=input("ingrese el apellido: ").lower()

            edad=0
            while(edad<1 or edad>110):
                try:
                    edad=(int(input("ingrese edad: ")))
                except:
                    print("solo puede ingresar un nro")
                
            sexof=""
            validacion=False
            while sexof not in ["Femenino","Masculino"]:
                sexo = input("Ingrese su tipo de sexo con una 'F' si es mujer o con una 'M' si es hombre: ").lower()
                if sexo == "f":
                    sexof = "Femenino"
                elif sexo == "m":
                    sexof = "Masculino" 

            correo = ""
            correo_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            while not re.match(correo_pattern, correo):
                correo = input("\tIngrese su correo electronico: ").lower()
            
            
            biblografia={
                    "codigo":codigo,
                    "nombre":nombre,
                    "apellido":apellido,
                    "sexo":sexof,
                    "correo":correo,
                    }
            
            registros.append(biblografia)

            input("enter para seguir")

        elif (opcion==2):
                system("cls")
                print("\t imprimir biografia")

                #generar lista para seleccionar que registro imprimir a txt
                print("\t Lista de registros")
                for i in range(len(registros)):
                    print(f"{i+1}. {registros[i]['nombre']}")
                try:
                    seleccion=int(input("\t Seleccione el registro que desea imprimir: "))
                    seleccion-=1
                    with open(f"{registros[seleccion]['nombre']}.txt","w") as archivo:#open(f"{ 'aqui va el directorio' registros[seleccion]['nombre']}.txt","w")
                        archivo.write(f"codigo: {registros[seleccion]['codigo']}\n")
                        archivo.write(f"nombre: {registros[seleccion]['nombre']}\n")
                        archivo.write(f"apellido: {registros[seleccion]['apellido']}\n")
                        archivo.write(f"sexo: {registros[seleccion]['sexo']}\n")
                        archivo.write(f"correo: {registros[seleccion]['correo']}\n")
                    print("\t Archivo creado")
                except:
                    print("registro no encontrado")
                input("enter para seguir")




        elif (opcion==3):
            system("cls")
            print("saliendo del programa")
            

          
    except:
        system("cls")
        print("solo puede ingresar un nro")