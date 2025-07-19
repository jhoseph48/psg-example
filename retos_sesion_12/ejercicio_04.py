edad_cliente = int(input("ingrese la edad del cliente:"))
monto_compra = float(input("ingrese el monto de compra"))

if edad_cliente > 60 and monto_compra > 1000:
    descuento = 0.2
elif edad_cliente > 18 and edad_cliente < 60 and monto_compra > 500:
    descuento = 0.1
else:
    descuento = 0.02

total_pagar = monto_compra - monto_compra*descuento
print("total a pagar:", total_pagar)