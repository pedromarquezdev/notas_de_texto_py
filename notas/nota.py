import usuarios.conexion

conectar = usuarios.conexion.conectar()
database = conectar[0]
cursor = conectar[1]

class Nota:
    
    def __init__(self, usuario_id, titulo ="",descripcion =""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):
        query ="INSERT INTO notas VALUES(null, %s,%s,%s,NOW())"
        
        #parametros de la consulta
        nota = (self.usuario_id, self.titulo, self.descripcion) 
        
        cursor.execute(query, nota)
        database.commit()
        
        return [cursor.rowcount, self]
    
    def listar(self):
        query = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        #query = "SELECT * FROM notas WHERE usuario_id = %s"
        #notasBUscadas = (self.usuario_id)
        
        cursor.execute(query)
        resultado = cursor.fetchall()
        
        return resultado
                
    def eliminar(self, titulo):
        query = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "
        cursor.execute(query)
        database.commit()
        
        return [cursor.rowcount,self]
        
        