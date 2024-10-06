import mysql.connector
#port puede ser 3306 o 3308

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_db_py",
        port=3306
    )
    """print para corroborar la conexión"""
    #print(database) 

    cursor = database.cursor(buffered=True)
    return [database,cursor]


"""Con la biblioteca mysql.connector con buffered True lo que buscamos es que los resultados
de las consultas que hacemos se almacenen en ese momento en la memoria.
sI buffered estuviese en False, como está por defecto, podríamos tener 
problemas al intentar ejecutar otra consulta mientras aún no hemos procesado
resultados anteriores"""