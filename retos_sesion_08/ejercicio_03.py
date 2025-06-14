#ingresa una pregunta por teclado y almacena el valor en una tupla
pregunta = tuple(input("realiza una pregunta"))

tupla = (("¿",)+pregunta+("?",))
print(tupla)
print(tupla*3)