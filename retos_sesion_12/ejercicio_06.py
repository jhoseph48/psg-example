entrada_usuario = input("Ingresa la operación (ejemplo 10, 5, +): ")

print("-------------")

partes = entrada_usuario.split(',')

if len(partes) != 3:
    print("Error de datos. Usa 'numero1, numero2, operacion'.")
else:
    num1 = float(partes[0].strip())
    num2 = float(partes[1].strip())
    operacion = partes[2].strip()

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    print(num1 / num2)
else:
    print("operador no reconocido")
