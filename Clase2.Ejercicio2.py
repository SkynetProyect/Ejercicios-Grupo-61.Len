#Area de un circulo dado su radio

def calcular_radio(radio=input("Escriba el radio del circulo: ")):
    respuesta = 3.1416*((float(radio))**2) # Incluye la formula del Area de un circulo en base a su radio.
    print("El Area es: ", respuesta)

calcular_radio() # Llama a la funcion
