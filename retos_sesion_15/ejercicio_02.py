class FrutaNoValidaError(Exception):
    pass

frutas_permitidas = {'🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑'}
canasta_de_frutas = []

print("Crea tu Canasta de Frutas")
print(frutas_permitidas)
print("Escribe 'salir' para terminar y ver tu canasta.")

while True:
    try:
        fruta_ingresada = input("Ingresa una fruta: ").strip()

        if fruta_ingresada.lower() == 'salir':
            break
        
        if fruta_ingresada not in frutas_permitidas:
            raise FrutaNoValidaError(fruta_ingresada)
        
        canasta_de_frutas.append(fruta_ingresada)

    except FrutaNoValidaError as e:
        print(e)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

print(canasta_de_frutas)
