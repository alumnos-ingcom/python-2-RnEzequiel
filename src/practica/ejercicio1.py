################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
Escribir una función que retorne True cuando un número entero es par
y False cuando no lo sea, sin utilizar módulo. (%)
"""

def es_par(numero:int):
    """
    Recibe un número entero como int y devuelve True si es par o
    False si es impar.
    """
    numero = abs(numero)
    while numero > 1:
        numero = numero - 2
    return numero == 0


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un número a verificar: "))
    if es_par(valor):
        print(f"{valor} es par.")
    else:
        print(f"{valor} es impar.")

if __name__ == "__main__":
    principal()
