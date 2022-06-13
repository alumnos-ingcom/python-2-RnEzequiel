################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la
suma de los dos anteriores. En la misma, los dos primeros términos son 1.
Implementar una función que permita obtener el n-esimo termino de la sucesión
de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""

def elemento_de_fibonacci(indice:int):
    """
    Recibe un número entero mayor a 2 como int y devuelve el número de la
    secuencia de Fibonacci correspondiente a dicha posición.
    """
    penultimo = 1
    ultimo = 1
    indice = indice - 2
    while indice > 0:
        penultimo, ultimo = ultimo, penultimo + ultimo
        indice = indice - 1
    return ultimo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese el índice del elemento a buscar: "))
    resultado = elemento_de_fibonacci(valor)
    print(f"El {valor}° numero de Fibonacci es {resultado}.")

if __name__ == "__main__":
    principal()
