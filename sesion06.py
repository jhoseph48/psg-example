print("tipos de datos booleanos")
print(True)
print(False)
print(True+True)
print(True*True)
print(True*False)
print(False+False)
print(False*False)
print("numeros y booleanos")
print(10+True)
print("declarar variables booleanas")
var_booleana = True
print(var_booleana)
pritn(type(var_booleana))
var_booleana = 0
print(var_booleana)
print(type(var_booleana))

print("operador de comparación")
print(10==10)
print(10 != 10)
print(10 < 10)
print(10 >= 10)
print(10 is 10)
print(10 is not 10)

print("asignacion de variables")
x = 10
mayor_que_cero = x > 0
print(mayor_que_cero)
diferente_de_10 = x != 10
print(diferente_de_10)

print("operadores logicos")
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not False)

print("operador NAND")
print(not (True and True))
print(not (True and False))

print("operador nor")
print(not (True or True))
print(not (True or False))

print("operador XOR")
a = True
b = False
print((a or b) and not (a and b))

print("ejemplo 1 comparacion y logicos")
numero = 20 
print( numero >= 0 and numero <= 100)

print("ejemplo 2 determinar si el est aprobo")
nota1 = 15
nota = 20
nota3 = 16
print((nota1 + nota2 + nota3) > 50)

print("ejemplo 3 determinar si 15 es divisible por 3 y 5 pero no por 2")
num1 = 15
print(num1 % 3 == 0 and num1 % 5 == 0 and num1 % 2 != 0)

