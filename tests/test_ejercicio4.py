################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 4.
"""

from practica.ejercicio4 import elemento_de_fibonacci


def test_elemento_de_fibonacci_3():
    """
    Verifica la devolución del tercer elemento de la secuencia de Fibonacci.
    """
    resultado = elemento_de_fibonacci(3)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 2

def test_elemento_de_fibonacci_4():
    """
    Verifica la devolución del cuarto elemento de la secuencia de Fibonacci.
    """
    resultado = elemento_de_fibonacci(4)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 3

def test_elemento_de_fibonacci_5():
    """
    Verifica la devolución del quinto elemento de la secuencia de Fibonacci.
    """
    resultado = elemento_de_fibonacci(5)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 5

def test_elemento_de_fibonacci_6():
    """
    Verifica la devolución del sexto elemento de la secuencia de Fibonacci.
    """
    resultado = elemento_de_fibonacci(6)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 8
