print("Ingresa dos números para realizar operaciones.")
print("Escribe 'salir' en cualquier momento para terminar.")

while True:
    try:
        entrada1 = input("Ingresa el primer número: ")
        if entrada1.lower() == 'salir':
            break
        num1 = float(entrada1)

        entrada2 = input("Ingresa el segundo número: ")
        if entrada2.lower() == 'salir':
            break

        num2 = float(entrada2)

        #Suma
        suma = num1 + num2
        print(f"Suma: {num1} + {num2} = {suma}")

        #Resta
        resta = num1 - num2
        print(f"Resta: {num1} - {num2} = {resta}")

        #Multiplicación
        multiplicacion = num1 * num2
        print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")

        #División
        try:
            division = num1 / num2
            print(f"División: {num1} / {num2} = {division}")
        except ZeroDivisionError:
            print("División: No se puede dividir entre cero.")

    except ValueError:
        print("❗ Error: Ingresa un valor numérico válido (ej. 5, 2.5).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")