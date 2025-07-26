print("Ingresa un número para verificar si es múltiplo de 7.")
print("Ingresa '0' para terminar el programa.")

while True:
    numero_ingresado = int(input("Ingresa un número: "))

    if numero_ingresado == 0:
        print("Número 0 ingresado. ¡Hasta luego!")
        break 

    if numero_ingresado % 7 == 0:
        print("El número", numero_ingresado, "SÍ es un múltiplo de 7.")
    else:
        print("El número", numero_ingresado, "NO es un múltiplo de 7.")
