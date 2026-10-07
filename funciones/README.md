# Funciones en Python 
Las funciones no permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario.
```python
# ejemplo deseamos crear un programa en python que nos permote sumar dos numeros.
numero_uno:int=45
numero_dos:int=70
suma:int=numero_uno+numero_dos
print(suma)
print(suma_dos)
```
Como hacemos reutilizable el ejercicio anterior mas lejible.
Para eso utilizaremos funcionen python es la siguiente:
1. Debe comenzar con la palabra reservada `def`.
2. Debe tener un nombre que de a entender que realizara la funcion.
3. Debera tener parametros y estos estaran encerrados en parentesistes `()`. No todaslas funciones resibiran parametros aun asi debera tener los `()`.
4. Las funciones deberan retomar datos a traves de la palabra reservada `return`.
```python
# Crear un programa que me permita sumar dos numeros 
def sumar(a:int,b:int):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```