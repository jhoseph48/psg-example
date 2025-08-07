def operacion(num1, num2, operador):
    if operador == "+":
        return num1+num2
    elif operador == "-":
        return num1-num2
    elif operador == "*":
        return num1*num2
    elif operador == "/":
        return num1/num2
    else:
        return "no se reconoce el operador"
    
suma = operacion(10,5,"+")
print(suma)