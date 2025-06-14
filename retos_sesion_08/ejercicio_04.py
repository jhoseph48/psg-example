#verificar si el estudiante aprobo segun sus notas
resultados = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

print("aprobo")
aprobo = sum(resultados)/len(resultados) > 50
print(aprobo)