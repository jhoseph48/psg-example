def vocales(cadena):
    nro_vocales = 0
    for i in cadena.lower():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            nro_vocales += 1
    return nro_vocales

print(vocales("CAdena"))