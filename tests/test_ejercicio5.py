################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas del ejercicio 5.
"""

from practica.ejercicio5 import balance_sintactico

def test_balance_sintactico_corchete_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de corchetes
    incompleta.
    """
    resultado = balance_sintactico("[[[]")
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_corchete_desordenada():
    """
    Verifica la devolución del valor False ante una cadena de corchetes
    desordenados.
    """
    resultado = balance_sintactico("][")
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_corchete_completa():
    """
    Verifica la devolución del valor True ante una cadena de corchetes
    completa.
    """
    resultado = balance_sintactico("[[ ]] [] })")
    assert isinstance(resultado, bool)
    assert resultado == True

def test_balance_sintactico_llave_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de llaves
    incompleta.
    """
    resultado = balance_sintactico("{{ }", False, llave = True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_llave_desordenada():
    """
    Verifica la devolución del valor False ante una cadena de llaves
    desordenadas.
    """
    resultado = balance_sintactico("{} }{", False, llave = True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_llave_completa():
    """
    Verifica la devolución del valor True ante una cadena de llaves completa.
    """
    resultado = balance_sintactico("{ {} {} }  [(", False, llave = True)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_balance_sintactico_parentesis_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de paréntesis
    incompleta.
    """
    resultado = balance_sintactico("()() (", False, parentesis = True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_parentesis_desordenada():
    """
    Verifica la devolución del valor False ante una cadena de paréntesis
    desordenadas.
    """
    resultado = balance_sintactico(")()(", False, parentesis = True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_parentesis_completa():
    """
    Verifica la devolución del valor True ante una cadena de paréntesis
    completa.
    """
    resultado = balance_sintactico("(( ()()) )  [{", False, parentesis = True)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_balance_sintactico_triple_corchete_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de corchetes,
    llaves y paréntesis donde los corchetes estén incompletos.
    """
    resultado = balance_sintactico("[ {} ()", True, True, True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_triple_parentesis_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de corchetes,
    llaves y paréntesis donde los peréntesis estén incompletos.
    """
    resultado = balance_sintactico("[] {} (", True, True, True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_triple_llave_incompleta():
    """
    Verifica la devolución del valor False ante una cadena de corchetes,
    llaves y paréntesis donde las llaves estén incompletas.
    """
    resultado = balance_sintactico("[] {{ } ()", True, True, True)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_balance_sintactico_triple_completa():
    """
    Verifica la devolución del valor True ante una cadena de corchetes,
    llaves y paréntesis completa.
    """
    resultado = balance_sintactico("{[()]} {} [()]", True, True, True)
    assert isinstance(resultado, bool)
    assert resultado == True
