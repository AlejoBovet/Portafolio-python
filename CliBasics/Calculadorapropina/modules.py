#Modulos para calcular la propina 

#importar modulo config
from config import divisas
#Conversores de moneda

def conversor(tipo_moneda,cantidad):
    if tipo_moneda == 'dolar':
        tipo_moneda = divisas['dolar']
    elif tipo_moneda == 'euro':
        tipo_moneda = divisas['euro']
    elif tipo_moneda == 'yen':
        tipo_moneda = divisas['yen']
    else:
        return 'Moneda no valida'
    
    return tipo_moneda * cantidad

#Calculadora de propina

def propina(cantidad,porcentaje):
    if porcentaje == 1:
        return cantidad * 0.1 + cantidad
    elif porcentaje == 2:
        return cantidad * 0.15 + cantidad
    elif porcentaje == 3:
        return cantidad * 0.2 + cantidad
    else:
        return 'Porcentaje no valido'
#Descuento especial cliente frecuente

def descuento(cantidad,tipo_cliente):
    if tipo_cliente == 'bronce':
        return  cantidad - cantidad * 0.1
    elif tipo_cliente == 'plata':
        return   cantidad - cantidad * 0.15
    elif tipo_cliente == 'oro':
        return  cantidad - cantidad * 0.2 
    else:
        return 'No hay descuento para este tipo de cliente'

