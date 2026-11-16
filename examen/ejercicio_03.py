## Type-hints (Anotaciones de tipo)
## Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) y retorne un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo estrictas vistas en el apunte.

def obtener_promedio(numeros: list[int])->float:
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Prueba de funcion
notas: list[int] = [14, 16, 18,]
print(f"Promedio: {obtener_promedio(notas)}")