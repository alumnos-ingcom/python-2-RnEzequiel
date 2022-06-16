################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes está
balanceada. Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.

Extra #1: Hacer que la funcion reciba que par de simbolos buscar si esta
balanceado. (como para pasar parentesis, llaves o cualquier otro)

Extra #2: Hacer que la función verifique el balanceo simultaneo de
parentesis, llaves y corchetes.
"""

def balance_sintactico(cadena, corchete = True, llave = False,
                        parentesis = False):
    """
    Recibe una cadena y tres valores booleanos opcionales que determinan si la
    función analizará en la cadena el balance de corchetes (opción
    predeterminada), llaves y/o paréntesis. La función analiza si cada par de
    símbolos está completo y ordenado, en cuyo caso devuelve el valor True. Si
    este no es el caso devuelve False.
    """
    balance = True
    cuenta_llave = 0
    cuenta_corchete = 0
    cuenta_parentesis = 0
    for caracter in cadena:
        if llave and caracter == "{":
            cuenta_llave += 1
        if llave and caracter == "}":
            cuenta_llave -= 1
        if corchete and caracter == "[":
            cuenta_corchete += 1
        if corchete and caracter == "]":
            cuenta_corchete -= 1
        if parentesis and caracter == "(":
            cuenta_parentesis += 1
        if parentesis and caracter == ")":
            cuenta_parentesis -= 1
        if cuenta_llave < 0 or cuenta_corchete < 0 or cuenta_parentesis < 0:
            balance = False
    if cuenta_llave > 0 or cuenta_corchete > 0 or cuenta_parentesis > 0:
        balance = False
    return balance


def principal():
    """
    Parte interactiva de la función.
    """
    frase = input("Ingrese cadena a analizar: ")
    resultado = balance_sintactico(frase, False, True)
    if resultado:
        print("La cadena está balanceada.")
    else:
        print("La cadena no está balanceada.")

if __name__ == "__main__":
    principal()
