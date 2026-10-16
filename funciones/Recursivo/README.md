### Recursividad en python 
# definicion
En Python, una función recursiva es aquella que se invoca a sí misma durante su ejecución para resolver un problema complejo mediante la resolución de versiones más pequeñas del mismo problema.
Este enfoque sigue la estrategia de "divide y vencerás", descomponiendo problemas hasta llegar a un caso base, que es la condición que detiene la recursión.

# Ejemplos en codigo 
```python
def suma_n(n):
    if n == 0:  # Caso base
        return 0
    else:  # Caso recursivo
        return n + suma_n(n - 1)
print(suma_n(5))  # Salida: 15
```
## Ejemplo de suma de una lista 

```python
def suma_recursiva(lista):
    """Suma todos los elementos de una lista recursivamente"""
    # Caso base: lista vacía
    if len(lista) == 0:
        return 0

    # Caso recursivo: primer elemento + suma del resto
    return lista[0] + suma_recursiva(lista[1:])

numeros = [1, 2, 3, 4, 5]
print(suma_recursiva(numeros))  # Output: 15
```