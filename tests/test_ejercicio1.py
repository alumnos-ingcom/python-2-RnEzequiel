################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 1.
"""

from practica.ejercicio1 import es_par


def test_es_par_verdadero_positivo():
    """
    Verifica la devolución del valor True ante un número par positivo.
    """
    resultado = es_par(4)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_par_verdadero_negativo():
    """
    Verifica la devolución del valor True ante un número par negativo.
    """
    resultado = es_par(-8)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_par_falso_positivo():
    """
    Verifica la devolución del valor False ante un número impar positivo.
    """
    resultado = es_par(1)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_es_par_falso_negativo():
    """
    Verifica la devolución del valor False ante un número impar negativo.
    """
    resultado = es_par(-25)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_es_par_cero():
    """
    Verifica la devolución del valor True ante un valor 0.
    """
    resultado = es_par(0)
    assert isinstance(resultado, bool)
    assert resultado == True
