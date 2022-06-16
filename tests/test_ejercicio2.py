################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 2.
"""

from practica.ejercicio2 import maximo_minimo_promedio


def test_maximo_minimo_promedio():
    """
    Verifica la devolución del valor máximo, mínimo y promedio de una secuencia.
    """
    resultado = maximo_minimo_promedio((1, 2, 0, 5, 2))
    assert isinstance(resultado, tuple)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], float)
    assert resultado == (5, 0, 2)

def test_maximo_minimo_promedio_vacio():
    """
    Verifica la devolución de valores 0 ante una secuencia vacía.
    """
    resultado = maximo_minimo_promedio(tuple())
    assert isinstance(resultado, tuple)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], float)
    assert resultado == (0, 0, 0.0)
