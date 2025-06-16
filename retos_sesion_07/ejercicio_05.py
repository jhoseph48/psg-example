#Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas
cadena = input("ingresa una linea texto:")
nueva_cadena = cadena.lower()
nueva_cadena = nueva_cadena.replace(" ", "")
resultado = (nueva_cadena == nueva_cadena[::-1])
print("es palindromo", resultado)
