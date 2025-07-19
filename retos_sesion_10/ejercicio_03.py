tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

clientes_fisica = set(tienda_fisica)
clientes_online = set(tienda_online)

compraron_en_ambos = clientes_fisica.intersection(clientes_online)
print("a:compraron en ambos", compraron_en_ambos)

solo_fisica = clientes_fisica.difference(clientes_online)
print("b:compraron solo en tienda física", solo_fisica)

solo_online = clientes_online.difference(clientes_fisica)
print("c:compraron solo en tienda online", solo_online)