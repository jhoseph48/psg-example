#segundos en semanas, dias , horas, minutos y segundos
segundos = 1000000


semanas = segundos // (60 * 60 * 24 * 7)
segundos %= (60 * 60 * 24 * 7)

dias = segundos // (60 * 60 * 24)
segundos %= (60 * 60 * 24)

horas = segundos // (60 * 60)
segundos %= (60 * 60)

minutos = segundos // 60
segundos %= 60


print(f"{semanas} semanas")
print(f"{dias} días")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")