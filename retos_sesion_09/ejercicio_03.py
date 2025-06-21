#Crear una lista de personas con 10 nombres de personas
#Obtener una sub lista de 5 a 9 con saltos de 2 en 2
#Buscar si existe el nombre "José" en la lista original
#Ordenar la sub lista alfabéticamente a-z
#Ordenar la lista original alfabéticamente descendente z-a

mi_lista = ["Ana", "José", "Carlos", "Barbara", "Zenon", "Teresa", "Luis", "Oscar", "Brandon", "Roxana"]
sub_lista = mi_lista[5:9:2]
print(sub_lista)
print("Esta José en la lista?", "José" in mi_lista)
print(sorted(sub_lista))
print(sorted(sub_lista, reverse=True))