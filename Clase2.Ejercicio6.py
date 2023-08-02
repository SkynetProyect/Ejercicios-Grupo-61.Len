#suma de numeros en lista dada


""" Funcion que crea la lista en base a cuantos numeros seran ingresados por el usuario"""


def creacion_array(tamanio=input("Ingrese el tamaño de la lista: ")):
    array = [None]*int(tamanio)
    for i in range(len(array)): #Asigna los numeros que el usuario digite en la lista
        numero = int(input("Ingrese el numero: "))
        array[i] = numero
    return array


""" Toma la lista ya hecha, suma sus componentes e imprime su resultado"""


def suma_lista():
    resultado = 0
    lista = creacion_array()
    for i in lista:
        resultado = resultado+i
    print(resultado)


suma_lista() #Llama la funcion que inicia el proceso
