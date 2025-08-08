class FondosInsuficientesError(Exception):
    pass

saldo_disponible = 500.00
limite_por_transaccion = 1000.00

print("--- 🏧 Bienvenido al Cajero Automático ---")
print(saldo_disponible)

while True:
    try:
        monto_str = input("Ingrese el monto a retirar (o 'salir' para finalizar): ")
        
        if monto_str.lower() == 'salir':
            break
        monto_a_retirar = float(monto_str)

        if monto_a_retirar > limite_por_transaccion:
            raise ValueError

        if monto_a_retirar > saldo_disponible:
            raise FondosInsuficientesError

        saldo_disponible -= monto_a_retirar
        print("¡Transacción finalizada!")
        break

    except ValueError as e:
        print(f"Error: {e}. Por favor, intente de nuevo.")
    
    except FondosInsuficientesError as e:
        print(f"Error: fondos insuficientes {e}")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")