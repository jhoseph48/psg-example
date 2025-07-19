prendas_deportivas = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
prendas_formales = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

conjunto_deportivo = set(prendas_deportivas)
conjunto_formal = set(prendas_formales)

inventario_tienda = conjunto_deportivo.union(conjunto_formal)

print(inventario_tienda)