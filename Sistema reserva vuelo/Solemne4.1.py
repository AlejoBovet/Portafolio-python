import Funciones as ut
from os import system
registros=[]
Adisponible=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,]

system("cls")
opcion=0
while opcion!=5:
    try:
        opcion=int(input("\tMenu\n1) Ver asientos disponibles\n2) Comprar asiento\n3) Anular vuelo\n4) Modificar datos de pasajero\n5) Salir\nIngrese su opcion aqui:---> "))
    except:
        print("Solo se aceptan numeros")
        system("cls")
    if opcion==1:
        system("cls")
       
        print("\tAsientos")
        print(f"|{Adisponible[1]}  {Adisponible[2]}  {Adisponible[3]}    {Adisponible[4]}  {Adisponible[5]}  {Adisponible[6]} |")
        print(f"|{Adisponible[7]}  {Adisponible[8]}  {Adisponible[9]}    {Adisponible[10]} {Adisponible[11]} {Adisponible[12]}|")
        print(f"|{Adisponible[13]} {Adisponible[14]} {Adisponible[15]}   {Adisponible[16]} {Adisponible[17]} {Adisponible[18]}|")
        print(f"|{Adisponible[19]} {Adisponible[20]} {Adisponible[21]}   {Adisponible[22]} {Adisponible[23]} {Adisponible[24]}|")
        print(f"|{Adisponible[25]} {Adisponible[26]} {Adisponible[27]}   {Adisponible[28]} {Adisponible[29]} {Adisponible[30]}|")
        print("|-------    --------|")
        print(f"|{Adisponible[31]} {Adisponible[32]} {Adisponible[33]}   {Adisponible[34]} {Adisponible[35]} {Adisponible[36]}|")
        print(f"|{Adisponible[37]} {Adisponible[38]} {Adisponible[39]}   {Adisponible[40]} {Adisponible[41]} {Adisponible[42]}|")

        input("Presione enter para continuar")

    elif opcion==2:
        AAreservar=0
        try:
            AAreservar=int(input("Ingrese un asiento a reservar: "))
        except:
            print("Ingrese un asiento vaido")
        del Adisponible [AAreservar]
        Adisponible.insert(AAreservar,'X')
        system("cls")
        print("\tAsientos")
        print(f"{Adisponible[1]}  {Adisponible[2]}  {Adisponible[3]}    {Adisponible[4]}  {Adisponible[5]}  {Adisponible[6]}")
        print(f"{Adisponible[7]}  {Adisponible[8]}  {Adisponible[9]}    {Adisponible[10]} {Adisponible[11]} {Adisponible[12]}")
        print(f"{Adisponible[13]} {Adisponible[14]} {Adisponible[15]}   {Adisponible[16]} {Adisponible[17]} {Adisponible[18]}")
        print(f"{Adisponible[19]} {Adisponible[20]} {Adisponible[21]}   {Adisponible[22]} {Adisponible[23]} {Adisponible[24]}")
        print(f"{Adisponible[25]} {Adisponible[26]} {Adisponible[27]}   {Adisponible[28]} {Adisponible[29]} {Adisponible[30]}")
        print("--------   --------")
        print(f"{Adisponible[31]} {Adisponible[32]} {Adisponible[33]}   {Adisponible[34]} {Adisponible[35]} {Adisponible[36]}")
        print(f"{Adisponible[37]} {Adisponible[38]} {Adisponible[39]}   {Adisponible[40]} {Adisponible[41]} {Adisponible[42]}")

        input("Presione cualquier tecla para continuar")
        system("cls")

        if(AAreservar>=1 and AAreservar <=30):
            pago=74000
            print(f" Su asiento es el numero {AAreservar}, con un costo de {pago}")
        elif(AAreservar>=31 and AAreservar <=42):
            pago=240000
            print(f" Su asiento es el numero {AAreservar}, con un costo de {pago}")
        else:
            print("ingresar un asiento valido")

        Nombre=cambiodenombre1=ut.nombre2()

        rut=rutingreso=ut.rut2()

        telefono=cambiodenumero1=ut.cambiodenumero2()

        var=int(input("Ingrese el numero correspondiente a su banco:\n1) Banco de Chile\n2) Banco Falabella\n3) BancoEstado\n4) Banco BBVA\n5)  Banco Santander\n6) Banco Duoc\nIngrese su opcion aqui:---> "))

        if var==6:
            desc=(pago*15)/100
            pagoD=pago-desc

            print(f"Por ser parte de Banco Duoc se le ha realizado un 15% de descuento, su nuevo monto a pagar es :{pagoD}")
        input("Presione cualquier tecla para continuar")

        if var==1:
            banco="Banco de Chile"
        elif var==2:
            banco= "Banco Falabella"
        elif var==3:
            banco="BancoEstado"
        elif var==4:
            banco="Banco BBVA"
        elif var==5:
            banco="Banco Santander"
        elif var==6:
            banco="Banco Duoc"

        Diccionario={
            "Nombre":Nombre,
            "Run":rut,
            "Telefono":telefono,
            "Banco":banco,
            "asientoreservado":AAreservar,
                    }

        Adisponible.append(Diccionario)
        registros.append(Diccionario)
        print(Diccionario)

    elif opcion==3:
        print("ingrese su asiento a anular")

        BuscarAAreservardo=0
        try:
            BuscarAAreservardo=int(input("Ingrese un asiento a anular: "))
        except:
            print("Ingrese un asiento valido")
        
        for datoguardado in registros:
            asientoreservado=datoguardado.get('asientoreservado')

            if asientoreservado==BuscarAAreservardo:
                registros.remove(Diccionario)
                del Adisponible [asientoreservado]
                Adisponible.insert(BuscarAAreservardo,BuscarAAreservardo)
    
    elif opcion==4:

        BuscarAAreservardo=0
        try:
            BuscarAAreservardo=int(input("Ingrese un asiento a revisar: "))
        except:
            print("Ingrese un asiento valido")

        rutABuscar=0                
        while(rutABuscar <3000000 or rutABuscar >99999999):
            try:
                rutABuscar=int(input("ingrese el numero de run, sin dígito verificador: "))
                if(rut!=rutABuscar):
                    print("ingrese un rut registrado")
                else:
                    ("rut registrado")

            except:
                print("solo puede ingresar un nro")
                
            for datoGuardado in registros: 
                runGuardado=datoGuardado.get("run")
                
            for datoguardado in registros:
                asientoreservado=datoguardado.get('asientoreservado')

            if (runGuardado==rutABuscar) or (asientoreservado==BuscarAAreservardo):
               opcion2=0
               while opcion2!=4:
                    try:
                       opcion2=int(input("Seleccione el dato a modificar \n 1.modificar nombre \n 2.modificar numero de telefono \n 3.modificar nombre y numnero de telefono \n 4.volver al menu pricipal"))
                    except:
                        print("Solo se aceptan numeros")
                        system("cls")
                    
                    if opcion2==1:
                        system("cls")
                        Diccionario['Nombre']=cambiodenombre1=ut.nombre2()
                            
                    elif opcion2==2:
                        system("cls")
                        
                        Diccionario['Telefono']=cambiodenumero1=ut.cambiodenumero2()
                    
                    elif opcion2==3:
                        system("cls")
                        
                        Diccionario['Nombre']=cambiodenombre1=ut.nombre2()
                        Diccionario['Telefono']=cambiodenumero1=ut.cambiodenumero2() 
                        
                    
                    elif opcion2==4:
                        system("cls")
                        input("preione cualquier tecla para continuar")
                        print("datos modificados guardados")
                        print(registros)
                        
                        
                    else:
                        print("ingrese una opcion valida")

                   

            else:
                print("ingrese datos registrados")

            
            
    elif opcion==5:
        ("gracias por viajar en Vuelos-Duoc ")
        
    else:
        print("esa opcion no existe")

                




        


    

                










   










