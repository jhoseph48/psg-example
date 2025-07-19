usuarios = {"admin": "admin123",
            "user1": "user123",
            "user2": "user123",
            "user3": "user123"}


usuario_ingresado = input("ingresa el nombre de usuario")
contrasena_ingresada = input("ingresa la contraseña")

if usuario_ingresado in usuarios:
    if usuarios[usuario_ingresado] == contrasena_ingresada:
        print("Acceso aprobado")
    else:
        print("Acceso denegado")
else:
    print("El usuario interesado, no existe.")