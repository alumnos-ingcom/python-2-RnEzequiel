################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una encriptación de sustitución
simple. Esto significa que cada caracter se sustituye por otro caracter de
acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga unicamente
caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas
letras del abecedario se vuelva a las primeras letras.

Implementar una funcion que codifique un texto rotandolo una cantidad de
posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una cantidad de
posiciones ajustable.
"""

def rotar_caracter(caracter, indice):
    """
    Recibe una cadena de 1 caracter y un indice en forma de número; y devuelve
    otro rotando entre los demás caracteres de su mismo tipo la cantidad
    especificada por el índice.
    """
    codigo = ord(caracter[0])
    rango = (0, 0)
    if 48 <= codigo <= 57: #Números
        rango = (48, 57)
    elif 65 <= codigo <= 90: #Mayúsculas
        rango = (65, 90)
    elif 97 <= codigo <= 122: #Minúsculas
        rango = (97, 122)
    if rango != (0, 0):
        diferencia = rango[1] - rango[0] + 1
        # Saca el resto del indice codificado dividido por la amplitud del
        # conjunto al que pertenece.
        codigo = rango[0] + ((codigo + indice - rango[0]) % diferencia)
    return chr(codigo)

def cifrado_cesar(cadena, indice):
    """
    Recibe una cadena y un índice de codificación. Llama a la función
    rotar_caracter por cada carecter individual y devuelve la cadena
    codificada
    """
    cifrado = ""
    for car in cadena:
        cifrado += rotar_caracter(car, indice)
    return cifrado

def descifrado_cesar(cadena, indice):
    """
    Recibe una cadena y un índice de descodificación. Llama a la función
    rotar_caracter con el índice negativo para hacer la operación inversa
    a la codificación por cada carecter individual; y devuelve la cadena
    decodificada.
    """
    descifrado = ""
    for car in cadena:
        descifrado += rotar_caracter(car, -indice)
    return descifrado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    msg = input("Ingrese mensaje a cifrar: ")
    numero = int(input("Ingrese el índice de cifrado: "))
    resultado = cifrado_cesar(msg, numero)
    print(f"El mensaje cifrado es [{resultado}].")
    msg = input("Ingrese código a descifrar: ")
    numero = int(input("Ingrese el índice de cifrado: "))
    resultado = descifrado_cesar(msg, numero)
    print(f"El código descifrado es [{resultado}].")

if __name__ == "__main__":
    principal()
