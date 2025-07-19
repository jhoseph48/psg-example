arca_de_noe = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}
print(arca_de_noe)

arca_de_noe.update({
    "🐘": 2,  # Elefantes
    "🐼": 2,  # Pandas
    "🐧": 2   # Pingüinos
})
print(arca_de_noe)

iterador = iter(arca_de_noe.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

existe_dragon = "🐲" in arca_de_noe
print("¿Existe la especie 'dragon' 🐲 en el arca?", existe_dragon)

del arca_de_noe["🦄"]
print(arca_de_noe)

arca_de_noe["🦒"] = 2
print(arca_de_noe)

arca_de_noe.clear()
print(arca_de_noe)