




def cambiodenumero2():
    telefono=0
    while  (telefono< 1000000 or telefono > 999999999):
        try:
            telefono=int(input("Ingrese su numero de telefono: "))
        except:
            print("solo se admiten numeros")
    return telefono

def nombre2():
    nombre=""
    while(len(nombre)<1):
        nombre=input("Ingrese su nombre: ")
    return nombre

def rut2():
    rut=0
    while(rut < 3000000 or rut > 99999999):
        try:
            rut=int(input("Ingrese su rut sin digito verificador ni puntos: "))
        except:
            print("Solo se admiten numeros")
    return rut




    