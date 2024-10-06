import re

def emailValido(email):
    """Vamos a evaluar si el email que ingresamos cumple los reuisitos"""
    #Expresión regular para validar el email:
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    #Si el email que ingresamos coincide con la regex es válido
    if re.match(regex,email):
        return True;
    else:
        return False


def passwordValido(passw):
    """Vamos a evaluar la password pasada por parametro
    Esta password contendrá la siguiente regulación:
    Minimo 8 caracteres
    Maximo 15
    Al menos una letra mayúscula
    Al menos una letra minucula
    Al menos un dígito
    No espacios en blanco
    Al menos 1 caracter especial    
    
    """
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)(?!.*\s).{8,20}$'
    if(re.match(regex, passw)):
        return True
    else:
        return False


        
    