import usuarios.acciones

acciones = usuarios.acciones

while True:

    print("""
    Acciones disponibles:
        -registro
        -login
    """)

    accion = input("¿Qué quieres hacer?: ")
    accionARealizar = acciones.Acciones()

    if(accion == "registro"):
        accionARealizar.registro()
        break
    elif(accion == "login"):
        accionARealizar.login()
        break
    elif(accion != "registro" or accion != "login"):
        print("¡Debe ingresar una opción válida!")













