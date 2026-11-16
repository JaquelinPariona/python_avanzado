## Documentación (docstring)
##Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a su potencia. Añade un docstring completo que cumpla estrictamente con la advertencia del apunte:
# 1. Breve explicación.
# 2. Especificación y tipos de los parámetros.
# 3. Restricciones (ej. el exponente no debe ser negativo).
# 4. Características del valor que retorna.

def calcular_potencia(base: float, exponente: float) -> float:
    """
    Eleva un número base a un exponente y retorna el resultado.

    Parámetros
    base (float): Número base que se va a elevar.
    exponente (float): Exponente al que se elevará la base.

    Restricciones
    El exponente no debe ser negativo.

    Retorna
    float: El resultado de base elevado a exponente.
    """
    if exponente < 0:
        return 0.0
    return base ** exponente

print(calcular_potencia(2, 3))
print(calcular_potencia(5, 2))