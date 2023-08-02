#Numero mas grande o pequeño en lista dada

"""FUncion que crea la lista y asigna valores segun entrada del usuario"""

def creacion_lista():
    array = [None]*int(input("Tamanio de lista: "))
    for i in range(len(array)):
        array[i] = int(input("inserte entero: "))

    return array


"""Funcion que busca el menor y mayor de los valores de la lista"""


def busqueda_numero():
    minimo = 999999
    maximo = 0
    lista = creacion_lista()
    print(lista)
    for i in lista:
        if i < minimo:
            minimo = i
        elif i > maximo:
            maximo = i
        else:
            pass
    print("El minimo: ", minimo, "maximo: ", maximo)


busqueda_numero() #llama el proceso