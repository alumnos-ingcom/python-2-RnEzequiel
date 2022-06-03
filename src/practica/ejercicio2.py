################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que
procesan secuencias.
"""

def maximo_minimo_promedio(secuencia:tuple):
    """
    Recibe una secuencia de números entero como tuple y devuelve otra
    tuple de la sigiuente forma:
    (valor_máximo, valor_mínimo, valor_promedio)
    En caso de recibir una tuple vacía, devuelve tres valores 0.
    """
    maximo, minimo, promedio = 0, 0, 0.0
    if len(secuencia) > 0:
        maximo = secuencia[0]
        minimo = secuencia[0]
        indice = 0
        while indice < len(secuencia):
            if secuencia[indice] > maximo:
                maximo = secuencia[indice]
            if secuencia[indice] < minimo:
                minimo = secuencia[indice]
            promedio = promedio + secuencia[indice]
            indice = indice + 1
        promedio = promedio / len(secuencia)
    return maximo, minimo, promedio


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cantidad_de_valores = int(input("Defina cuántos valores se van a ingresar: "))
    secuencia_de_valores = tuple()
    while cantidad_de_valores > 0:
        nuevo_valor = float(input("Ingrese un valor: "))
        secuencia_de_valores = secuencia_de_valores + (nuevo_valor,)
        cantidad_de_valores = cantidad_de_valores - 1
    resultado = maximo_minimo_promedio(secuencia_de_valores)
    print(f"El mayor valor es {resultado[0]}")
    print(f"El menor valor es {resultado[1]}")
    print(f"El promedio de los valores es {resultado[2]}")

if __name__ == "__main__":
    principal()
