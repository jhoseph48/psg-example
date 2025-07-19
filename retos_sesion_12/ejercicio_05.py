nombre_contacto = input("Ingresa el nombre del contacto: ")

numero_telefono = input("Ingresa el número de teléfono (ejemplo 59171469794): ")

if nombre_contacto:
    if len(numero_telefono) == 11:
        print("Contacto guardado")
else: 
    print("Datos incorrectos")
nombre_es_valido = bool(nombre_contacto)
