# Pasar farenhait to celsius

def transformar_grados(number=input("Insertar los grados: ")):
    return ((int(number)) - 32) * (5 / 9)   #formular para pasar de F a C


print(transformar_grados()) #Imprime el resultado de la funcion
