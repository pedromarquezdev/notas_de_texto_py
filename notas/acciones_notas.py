import notas.nota as nota



class Acciones:
    
    def crear(self,usuario):
        print(f"Perfecto {usuario[1]}Vamos a crear una nueva nota.")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Escribe tu nota: ")
        
        notaCreada = nota.Nota(usuario[0], titulo, descripcion)
        guardar = notaCreada.guardar()
        
        if guardar:
            print(f"Perfecto has guardado la nota: {notaCreada.titulo}")
        else:
            print("No has podido crear la nota")
    
    def mostrar(self,usuario):
        #Para que combine mejor con la seccion de eliminar 
        #he decidodo borrar el print de la primer manena
        #print(f"Perfecto {usuario[1]}, aquí tienes tus notas: ")
        print(f"Aquí tienes tus notas: ")
        notasAMostrar = nota.Nota(usuario[0])
        notas = notasAMostrar.listar()
        if not notas:
            print ("No haz creado ninguna nota todavía.")
        
        for element in notas:
            print("***********************************")
            print(f"Título: {element[2]}. \n {element[3]}")
            
    def borrar(self, usuario):
        print(f"\n OK.{usuario[1]} vamos a borrar notas\n")
        self.mostrar(usuario)
        
        titulo = input("Introducuce el titulo de la nota a borrar: ")
        
        notaABorrar = nota.Nota(usuario[0], titulo)
        
        eliminar = notaABorrar.eliminar(titulo)
        
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {notaABorrar.titulo}")
        else:
            print("No se ha podido borrar la nota.")
    
        
        
        
        
                
        