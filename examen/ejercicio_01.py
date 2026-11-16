## Funciones Básicas
## Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo (números enteros o flotantes) y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado

def calcular_area_rectangulo(b, h):
    return b * h

# Pruebar con dos valores distintos
area1 = calcular_area_rectangulo(5, 10)
area2 = calcular_area_rectangulo(7.5, 4.2)

print(f"area 1: {area1}")
print(f"area 2: {area2}")