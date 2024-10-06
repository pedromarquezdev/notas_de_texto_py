import usuarios.conexion
import datetime
import hashlib

"""hashlib se utiliza para cifrar las contraseñas"""


conectar = usuarios.conexion.conectar()
database = conectar[0]
cursor = conectar[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        #cifrar la contraseña:
        cifrado = hashlib.sha256()
        #el metodo update recibe un byte asique tengo que pasarle
        #valores en bytes
        #con el médtodo enconde('utf8) me va a convertir el valor de
        #adentro a bytes
        cifrado.update(self.password.encode('utf8'))
        
        query = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        
        #no guardo self.password sino cifrado.hexdigets()
        #para poder guardar el cifrado hexadecimal que me ha generado la libreria
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(query, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0,self]
        
        return result
            
    
    def identificar(self):
        #Inicio de la consulta
        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #cifrado de clave
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        #parámetros de la consulta
        usuario = (self.email, cifrado.hexdigest())
        #ejecuciṕn de la consulta
        cursor.execute(query,usuario)
        #resultado de la consulta
        resultado = cursor.fetchone()
        
        #Comprobar el resultado de la consulta.
        #Si resultado es None (en caso de no haber contrado email y password)
        #entonces retornamos False y en caso que haya coincidencia retornamos
        #el resultado encontrado.  
               
        if resultado:
            return resultado
            
        else:
            print("El email o la contraseña son incorrectos.")            
            return False
    
    def comprobarUsuario(self):
        #Inicio de la consulta
        query = "SELECT * FROM usuarios WHERE email = %s"
        
        usuarioEmail = (self.email,)
        cursor.execute(query,usuarioEmail)
        resultado = cursor.fetchone()
        
        #comprobar si existe el email en la base de datos
        if  resultado:
            return True #el email existe
        else:
            return False #el email no existe
    
    
        
        
        
        
        
        
        

         