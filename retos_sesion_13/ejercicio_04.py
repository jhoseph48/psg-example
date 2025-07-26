print("Escribe una frase para verificar si es un palíndromo.")
print("Escribe 'salir' para terminar la ejecución.")

while True: 
    frase_original = input("Introduce una frase: ").strip()
    frase_procesada = frase_original.lower().replace(" ", "")

    if frase_procesada == "salir":
        break

    frase_invertida = frase_procesada[::-1]

    if frase_procesada == frase_invertida:
        print(frase_original, "SÍ es un palíndromo.")
    else:
        print(frase_original, "NO es un palíndromo.")