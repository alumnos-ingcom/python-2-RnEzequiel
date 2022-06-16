################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 3.
"""

from practica.ejercicio3 import superposicion


def test_superposicion_extension():
    """
    Verifica la devolución de la cantidad de caracteres de la superposicion.
    """
    resultado = superposicion(list("Hola Mundo"), list("Hola"))
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 4

def test_superposicion_inicio():
    """
    Verifica la devolución del indice del inicio de la superposicion.
    """
    resultado = superposicion(list("012345Texto"), list("Texto"), \
                              extension = False, inicio = True)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 6

def test_superposicion_orden():
    """
    Verifica el orden de devolución de los valores de extensión e inicio.
    """
    resultado = superposicion(list("Esta es una frase"), \
                              list("La torta es una mentira"), inicio = True)
    assert isinstance(resultado, tuple)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert resultado == (10, 2)

def test_superposicion_nulo():
    """
    Verifica la devolución de los valores de extensión 0 e inicio None ante dos
    listas sin elementos en común.
    """
    resultado = superposicion(list("Uno"), list("Tres"), inicio = True)
    assert isinstance(resultado, tuple)
    assert isinstance(resultado[0], int)
    assert resultado == (0, None)
