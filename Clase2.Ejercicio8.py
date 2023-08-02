#funcion que invierte el orden de los elementos en una lista dada.

"""FUncion que crea la lista y asigna valores segun entrada del usuario"""
"""Luego la invierte usando la funcion reverse y retorna la lista"""


def creacion_lista():
    array = [None]*int(input("Tamanio de lista: "))
    for i in range(len(array)):
        array[i] = int(input("inserte entero: "))
    array.reverse()
    print(array)

creacion_lista()
