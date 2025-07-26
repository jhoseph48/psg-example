filas = 8
columnas = 8

for i in range(filas):
    fila_actual = ""
    for j in range(columnas):
        if (i + j) % 2 == 0:
            fila_actual += "# " 
        else:
            fila_actual += "* " 
    
    print(fila_actual)