#construir el operador XNOR en python
print("XNOR")
a = False
b = False
print(a and b or (not a and not b))
a = False
b = True
print(a and b or (not a and not b))
a = True
b = False
print(a and b or (not a and not b))
a = True
b = True
print(a and b or (not a and not b))