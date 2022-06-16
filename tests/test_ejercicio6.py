################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 6.
"""

from practica.ejercicio6 import rotar_caracter, cifrado_cesar, \
descifrado_cesar

def test_rotar_caracter_desconocido():
    """
    Verifica la devolución de un mismo caracter que no sea letra o número sin
    rotar.
    """
    resultado = rotar_caracter("+", 4)
    assert isinstance(resultado, str)
    assert resultado == "+"

def test_rotar_caracter_positivo():
    """
    Verifica la devolución de un caracter rotado un número positivo de
    posiciones.
    """
    resultado = rotar_caracter("A", 4)
    assert isinstance(resultado, str)
    assert resultado == "E"

def test_rotar_caracter_negativo():
    """
    Verifica la devolución de un caracter rotado un número negativo de
    posiciones.
    """
    resultado = rotar_caracter("9", -3)
    assert isinstance(resultado, str)
    assert resultado == "6"

def test_rotar_caracter_mayuscula_vuelta_positiva():
    """
    Verifica la devolución de un caracter mayúscula rotado por sobre el
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("Y", 5)
    assert isinstance(resultado, str)
    assert resultado == "D"

def test_rotar_caracter_mayuscula_vuelta_negativa():
    """
    Verifica la devolución de un caracter mayúscula rotado por debajo del
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("B", -2)
    assert isinstance(resultado, str)
    assert resultado == "Z"

def test_rotar_caracter_minuscula_vuelta_positiva():
    """
    Verifica la devolución de un caracter minúscula rotado por sobre el
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("a", 28) #26(vuelta) + 2
    assert isinstance(resultado, str)
    assert resultado == "c"

def test_rotar_caracter_minuscula_vuelta_negativa():
    """
    Verifica la devolución de un caracter minúscula rotado por debajo del
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("e", -55) # -26- 26 -3
    assert isinstance(resultado, str)
    assert resultado == "b"

def test_rotar_caracter_numerico_vuelta_positiva():
    """
    Verifica la devolución de un caracter numérico rotado por sobre el
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("5", 5)
    assert isinstance(resultado, str)
    assert resultado == "0"

def test_rotar_caracter_numerico_vuelta_negativa():
    """
    Verifica la devolución de un caracter numérico rotado por debajo del
    límite de posiciones de su conjunto.
    """
    resultado = rotar_caracter("2", -3)
    assert isinstance(resultado, str)
    assert resultado == "9"

def test_cifrado_cesar():
    """
    Verifica la devolución de una cadena cifrada completa.
    """
    resultado = cifrado_cesar("Abc 123 xyZ", 2)
    assert isinstance(resultado, str)
    assert resultado == "Cde 345 zaB"

def test_descifrado_cesar():
    """
    Verifica la devolución de una cadena descifrada completa.
    """
    resultado = descifrado_cesar("123BCde", 1)
    assert isinstance(resultado, str)
    assert resultado == "012ABcd"

def test_cifrado_y_descifrado_cesar():
    """
    Verifica la devolución de una cadena completa tras ser cifrada y
    descifrada.
    """
    cadena = cifrado_cesar("Mensaje a ser cifrado n° 2659", 84)
    resultado = descifrado_cesar(cadena, 84)
    assert isinstance(resultado, str)
    assert resultado == "Mensaje a ser cifrado n° 2659"

