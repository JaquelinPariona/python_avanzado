#  En la siguiente funcion deberan escribir la documentacion sugun la convencion para el docstring de funciones.
def area_rectangulo(b,h):
    """
    calcula el area del rectangulo de dos numeros

    Args:
    b(int|float): este argumento sera la base del rectangulo
    h(int|float): este argumento sera la altura del rectangulo

    Raises:
    los argumentos no podran ser igual o menores a 0

    Return:
    int|float: el resultado de la operacion b*h (base*altura)
    """
    return b*h


# Funcion para hallar la potencia de un numero
def potencia(n:int,p:int)->int:
 """
    calcula la potencia con dos numeros

    Args:
    n(int): este argumento sera la base del rectangulo
    p(int): este argumento sera la altura del rectangulo

    Raises:
    los argumentos no podran ser igual o menores a 0

    Return:
    int: el resultado de la operacion b*h (base*altura)
    """
    resultado:int=1
    for _ in range(p):
        resultado *= n
    return resultado



