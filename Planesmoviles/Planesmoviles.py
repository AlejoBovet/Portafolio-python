from os import system


import random
opcion=0
registroCliente=[]
MBreal=0

system("cls")
while(opcion!=4):

    print("\t Menu de Calera de tango net ")
    print("\t1.  Registro Cleinte")
    print("\t2.  Descontar MB")
    print("\t3.  Consultar datos de un cliente")
    print("\t4.  salir")

    try:
        opcion=int(input("ingrese su opcion "))
        
        if (opcion==1):
            system("cls")
            print("\t Registro cliente")

            codigo= random.randint(5000,15000)

            run=0    
            while(run <3000000 or run >99999999):
                try:
                    run=int(input("ingrese el numero de run, sin dígito verificador: "))
                except:
                    print("solo puede ingresar un nro")
            
            nombre=""
            while(nombre==""):
                nombre=input("ingrese el nombre del cliente: ")
            
            apellido=""
            while(apellido==""):
                apellido=input("ingrese el apellido del cliente: ")

            edad=0
            while(edad<15 or edad>110):
                try:
                    edad=(int(input("ingrese edad cliente: ")))
                except:
                    print("solo puede ingresar un nro")
            
            sexo=0
            validacion=False
            while(validacion==False):
                sexo=input("Ingrese su tipo de sexo con una 'F' si es mujer o con una 'M' si es hombre: ")
                if(sexo.lower()== "f" or sexo.lower()== "m"):
                        validacion=True
                else:
                    validacion=False
                if(sexo.lower()=="f"):
                    sexof="Femenino"
                elif(sexo.lower()=="m"):
                    sexof="Masculino"

            correo=""
            while(correo.find("@")==-1) or (correo.find(".")==-1):
                correo=input("\t ingrese el correo del cliente: ")

            Plan=""
            while(Plan.upper()!="ESTUDIANTE" and Plan.upper()!="EMPRESARIO" and Plan.upper()!="FELIZ"):
                Plan=input("\t Ingrese el tipo de plan contratado: ")
            
            MBinicial=10000
            print("Su cantidad total de MB es de 10000")

            cliente={
                "codigo":codigo,
                "run":run,
                "nombre":nombre,
                "apellido":apellido,
                "sexo":sexo,
                "correo":correo,
                "Plan":Plan,
                "MBinicial":MBinicial
                }

            registroCliente.append(cliente)

            input("enter para seguir")


        elif (opcion==2):
            system("cls")
            print("\t Descontar MB")

            runABuscar=0                
            while(runABuscar <3000000 or run >99999999):
                try:
                    runABuscar=int(input("ingrese el numero de run, sin dígito verificador: "))
                    if(run!=runABuscar):
                        print("ingrese un rut registrado")
                    else:
                        ("rut registrado")

                except:
                    print("solo puede ingresar un nro")
                    

            for datoGuardado in registroCliente:
                
                runGuardado=datoGuardado.get("run")
                if runGuardado==runABuscar:
                    MBusado=-1
                    while(MBusado<0 or MBusado>10000):
                        try:
                            MBusado=int(input("Ingrese la canitdad de mb usado, recuerde que no puede sobrepsarb los 10.000mb"))
                        except:
                            print("Recuerdo que los MB usados no pueden pasar el MB total")
                            MBreal=MBinicial-MBusado
                        print(f"su total de MB es de: {MBreal}")

            Cliente2={
                "codigo":codigo,
                "run":run,
                "nombre":nombre,
                "apellido":apellido,
                "sexo":sexo,
                "correo":correo,
                "Plan":Plan,
                "MBreal":MBreal,
                }
                        
        elif (opcion==3):
            system("cls")
            print("\t Consultar datos de un cliente")

            runABuscar=0                
            while(runABuscar <3000000 or run >99999999):
                try:
                    runABuscar=int(input("ingrese el numero de run, sin dígito verificador: "))
                    if(run!=runABuscar):
                        print("ingrese un rut registrado")
                    else:
                        ("rut registrado")

                except:
                    print("solo puede ingresar un nro")

            print(Cliente2)

        elif (opcion==4):
            system("cls")
            print("Gracias por utilizar la aplicación")
            
        else:
            ("esa opcion no existe ")
    except:
        system("cls")
        print("solo puede ingresar un nro")



