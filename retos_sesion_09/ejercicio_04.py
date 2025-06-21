#Una dulcería tiene 2 listas una con los productos y otra con los precios
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Papitas", "Coca Cola"]
Precios = [2.5, 3, 1, 10, 18]

#Agregar 2 productos nuevos al final de las listas
productos.append("Galletas")
productos.append("Alfafor")
print(productos)

#Eliminar el producto con el nombre "Bon Bon Bum" de las listas
productos.remove("Bon Bon Bum")
print(productos)

#¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
oreo = productos.index("Oreo")
chizitos = productos.index("Chizitos")
print("el precio del producto oreo es: ", Precios[oreo])
print("el precio del producto chizito es: ", Precios[chizitos])

#¿Cuál es el producto más caro y el más barato?
print(productos[Precios.index(max(Precios))])
print(productos[Precios.index(min(Precios))])

#¿Cuántos productos tienes en total?
print(len(productos))
print(productos)

#¿Cuanto cuestan todos los productos?
print("todos los productos le saldrian por un precio de: ", sum(Precios))

#Ordena los productos y precios del más barato al más caro
productos.sort()
print(productos)
Precios.sort()
print(Precios)

#Eliminar todos los productos de las listas
productos.clear()
print(productos)