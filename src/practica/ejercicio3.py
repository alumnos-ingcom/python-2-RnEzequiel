################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos
listas. Siendo 0 sin superposición y uno para cada elemento superpuesto.
Extra #1
Indicar en lugar de la cantidad de caracteres superpuestos, la posicion
de inicio de la superposición.
"""

def superposicion(lista_uno, lista_dos, extension = True, inicio = False):
    """
    Recibe dos listas además de dos booleanos opcionales extension e inicio,
    y busca la mayor secuencia de elementos consecutivos coincidentes entre
    ambas listas.
    Si extension es True (predeterminado), devuelve la cantidad de elementos
    que conforman dicha secuencia en forma de int.
    Si inicio es True, devuelve el indice del primer caracter de la primer
    lista donde comience la secuencia en forma de int. En caso de que no haya
    elementos comunes entre ambas listas, devuelve None.
    Si tanto extension como inicio son True, se devuelven ambos resultados
    de la forma especificada en forma de tuple (extension, inicio)
    """
    maxima_superposicion = 0
    inicio_maxima_superposicion = None
    indice_uno = 0
    while indice_uno < len(lista_uno):
        indice_dos = 0
        while indice_dos < len(lista_dos):
            superpos = 0
            # Revisa cuántos elementos conecutivos a partir del indice
            # coinciden sin salirse del rango de ninguna lista
            while indice_uno + superpos < len(lista_uno) and \
                  indice_dos + superpos < len(lista_dos) and \
                  lista_uno[indice_uno + superpos] == \
                  lista_dos[indice_dos + superpos]:
                superpos = superpos + 1
            if superpos > maxima_superposicion:
                maxima_superposicion = superpos
                inicio_maxima_superposicion = indice_uno
            indice_dos = indice_dos + 1
        indice_uno = indice_uno + 1
    if extension and inicio:
        return (maxima_superposicion, inicio_maxima_superposicion)
    elif extension:
        return maxima_superposicion
    elif inicio:
        return inicio_maxima_superposicion


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista_uno = list(input("Ingrese una frase: "))
    lista_dos = list(input("Ingrese otra frase: "))
    resultado = superposicion(lista_uno, lista_dos, inicio=True)
    print(resultado)

if __name__ == "__main__":
    principal()
