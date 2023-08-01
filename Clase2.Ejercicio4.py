#Numero par o Impar

def analizar_numero(numero=input("Ingrese Numero Entero: ")):
    proceso = (-1)**(int(numero)) #Convierte la entrada de Str a Int para ser operada y calcula si es par o impar

    if proceso == 1: #Confirma que tipo de numero es y da la primer respuesta en caso de que sea par
        print("Es par.")
    else:
        print("Es impar.") #En caso de ser impar, provisiona esta respuesta


analizar_numero() #Llama la funcion
