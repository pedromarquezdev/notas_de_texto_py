import validaciones.validations
import usuarios.usuario as usuario
#as user
import notas.acciones_notas

validations = validaciones.validations

class Acciones:
    
    def registro(self):
        print("Vamos a registrarte en el sistema...")
        nombre = input("Ingresa tu nombre: ")
        apellido= input("Ingresa tu/s apellido/s: ")
        while True: 
            email = input("Ingresa tu email: ")
            if(not validations.emailValido(email)):
                print("Debe ingresar un email válido.")

            else:
                break
            
        while True:
            password = input("Ingresa tu clave: ")
            if(not validations.passwordValido(password)):
                print("Debes ingresar una clave correcta.")
                print("""
                Con los siguientes parámetros:
                Minimo 8 caracteres
                Maximo 15
                Al menos una letra mayúscula
                Al menos una letra minucula
                Al menos un dígito
                No espacios en blanco
                Al menos 1 caracter especial 
                 """)
            else:
                break;
        usuarioCreado = usuario.Usuario(nombre, apellido, email, password)
        #comprobarEmail = usuarioCreado.identificar()
        
        if usuarioCreado.comprobarUsuario():
            print("El usuario ya existe!")
        elif not usuarioCreado.comprobarUsuario() :
            registro = usuarioCreado.registrar()

            if registro[0] >= 1:
                print(f"Perfecto {registro[1].nombre} te has registrado exitosmente!")
            else:
                print("No te has registtrado correctamente...")

    def login(self):
        print("Ingresa al sistema...")
        while True: 
            email = input("Ingresa tu email: ")
            if(not validations.emailValido(email)):
                print("Debe ingresar un email válido.")
            else: 
                break
        password = input("Ingresa tu contraseña: ")
        
        usuarioLog = usuario.Usuario("","",email, password)
              
        
        login = usuarioLog.identificar()
        if login:
             print(f'Bienvenido {login[1]} has ingresado en el sistema el {login[5]}')
             self.siguientesAcciones(login)
        else:
            print("No puedes ingresar.")
            print("Intenta nuevamente.")
            #pedir que se ejecute de nuevo el lo
            # gin para ingresar el email
            #nuevamente hasta que el ingreso se realice 
            #↓↓↓
            #self.login()
    
    def siguientesAcciones(self, usuario):
        print("""
              Acciones disponibles:
              -Crear nota(crear)
              -Mostrar nota(mostrar)
              -Eliminar nota(eliminar)
              -Salir(salir)
              """)
        accion = input("¿Qué deseas hacer? \n → ")
        accion_de_notas = notas.acciones_notas.Acciones()
        
        
        if accion == "crear":
            accion_de_notas.crear(usuario)
            #volver a mostrar las opciones
            self.siguientesAcciones(usuario)
        elif accion == "mostrar":
            accion_de_notas.mostrar(usuario)
             #volver a mostrar las opciones
            self.siguientesAcciones(usuario)
        elif accion == "eliminar":
            accion_de_notas.borrar(usuario)
             #volver a mostrar las opciones
            self.siguientesAcciones(usuario)
        elif accion == "salir":
            print(f"¡{usuario[1]} hasta pronto!")
            exit()
        else:
            print("Selecciona la opción correcta")
             #volver a mostrar las opciones
            self.siguientesAcciones(usuario)
        return None
           
        
        
        
