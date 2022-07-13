"""3.	El nuevo sistema de taxis LUBER requiere usted desarrolle un programa en Python, que permita determinar el valor del viaje, considerando el valor del kilómetro 
por tipo de vehículo. Para lo anterior, se debe elegir un único tipo de vehículo e ingresar la cantidad total 
de kilómetros recorridos

Al finalizar el programa debiera desplegar la boleta, cuyo ejemplo se muestra a continuación:

		Tipo de Vehículo: Sedan
Total de KM: 5
El total de su boleta es: $6500"""

print("bienvenido a luber")

distancia=float(input("indique la distancia recorrida en Km por favor"))

Costocoupe=800*distancia
costosedan=1300*distancia
costovan=2000*distancia

#coupe=800
#sedan=1300
#van=2000

vehiculo=input("indique el tipo de vehiculo sedan, coupe o van")

if(vehiculo=="coupe"):
    print(f"tipo de vehiculo {vehiculo}")
    print(f"total de km {distancia:,.2f}")
    print(f"El total de su boleta es:${Costocoupe}")
elif(vehiculo=="sedan"):
    print(f"tipo de vehiculo {vehiculo}")
    print(f"total de km {distancia:,.2f}")
    print(f"El total de su boleta es:${costosedan}")
elif(vehiculo=="van"):
    print(f"tipo de vehiculo {vehiculo}")
    print(f"total de km {distancia:,.2f}")
    print(f"El total de su boleta es:${costovan}")
else:
    print("ingrese uno de los vehiculos mencionados por favor")










