### Programa para contar los parentesis dentro de una lista

lista = ['(())', '()()', '(()', '())', '()']

# definimos la funcion 
def contar_parentesis(lista):
    # inicializamos los contadores
    Parentesis = 0
    # recorremos la lista
    for cadena in lista:
        # recorremos la cadena
        for c in cadena:
            # si encontramos un parentesis
            if c == '(' or c == ')':
                Parentesis += 1
    # devolvemos el resultado
    return Parentesis

# recorremos la lista
print(contar_parentesis(lista))  # imprimimos el resultado






