estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for nombre, nota in estudiantes:
    if nota >= 51:
        print("¡Felicidades!", nombre, "Has aprobado el curso con una nota de:", nota)