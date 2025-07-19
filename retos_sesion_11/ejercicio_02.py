alimentos_animales = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}
print(alimentos_animales)

alimentos_animales.update(
    leche=["gato", "perro"],
    pasto=["vaca", "conejo"],
    semillas=["pájaro", "pato"],
    manzana=["caballo"]
)

print(alimentos_animales)

existe_trigo = 'trigo' in alimentos_animales
print("¿Existe 'trigo' en el diccionario?", existe_trigo)

del alimentos_animales['zanahoria']

print(alimentos_animales)