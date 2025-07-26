contador = 0
numero_actual = 1


while contador < 20:
    if numero_actual % 10 == 0:
        print((contador + 1), numero_actual)
        contador += 1
    
    numero_actual += 1
