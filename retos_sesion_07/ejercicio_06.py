print("1 str.title()")
cadena1 = "este es un titulo"
cadena1 = cadena1.title()
print(cadena1)

print("2 str.islower()")
cadena2 = "hola mundo"
cadena2 = cadena2.islower()
print("is lower", cadena2)

print("3 str.isupper()")
cadena3 = "PYTHON"
cadena3 = cadena3.isupper()
print("is upper", cadena3)

print("3 str.join()")
separador = "-"
palabras = ["manzana", "pera", "uva"]
fruta_unida = separador.join(palabras)
print(fruta_unida)

print("4 str.partition()")
cadena4 = "Hola mundo, esto es un ejemplo."
separador = "mundo"
partes = cadena4.partition(separador)
print(partes)

print("5 str.rsplit()")
cadena5 = "manzana,pera,uva,platano"
resultado_completo = cadena5.rsplit(',')
print(resultado_completo)