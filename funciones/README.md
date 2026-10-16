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
## Funciones avanzadas 
Existe tres grandes conceptos para poder entender el uso avanzada de las funciones:
1. Argumentos, parametros posicionales y nominales,*args y +kargs*.
2. Anotaciones en la salida de una funcion.
3. Recursividad.

```python 
# Anotacion en una funcion
def suma(a:int,b:float)->int:
    return a+b

# Crear una funcion que resiva cuatro numeros enteros y como salida que me muestre los 4 numeros enteros en una lista 

def numeros_lista(a:int, b:int, c:int, d:int)->list[int]:
    return [a, b, c, d]

```
**Argumentos Parametros**
**Parametros** - Los parametros son las variables que se declaran en la definicion  de la funcion.
**Argumentos** - es el dato concreto enviado en el llamado de la funcion.
**Nota:** En ambos casos tenemos los posicionale nominales.
```python
# Parametros
def suma(a,b): # En este caso tenemos uan funcion suma que recibe dos parametros a,b
suma(34,45) # En este caso estoy llamando a la funcion pasandole como argumentos de datos.
# en este caso concreto podemos decir que estamos frente a una funcion que tiene parametros posicionales, eso significa que cada valor reemplaza en el orden que le pasemos a las variables, 34->a, 45->b.
def login(usuario="",password=""):
    return "acceso correcto"
login(password="12345678",usuario="mia")
# Esta funcion es una funcion nominal por que para pasar los valores tengo que indicar la variable a la que se le va asociar en el parametro de la funcion.
```

