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


## Funciones anonimas 
Las funciones anonimas en python son llamadas `lambda` estas funciones tiene las siguientes propiedades: 
1. Se escribe en una unica sentencia `(linea)`.
2. No tiene nombre `(anonima)`.
3. Su cuerpo conlleva un `return` implicito.
4. Puede recibir cualquier numero de parametro.

La estructura para definir una funcion landa `lambda` es las siguientes
1. Escribir la palabra reservada `lambda`.
2. Especificar la cantidad de parametros.
3. Indicar los datos de retorno.
```python 
lambda a,b: a+b

```
> [!TIP] Puesto que esta funcion es anonima para ejecutarla debemos almacenar la funcion en la variable 
```python 
suma=lambda a,b: a+b
suma(3,6)
```
# Documentacion
Python nos permite documentar la funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para eso usamos una cade de texto despues de la definicion de una funcion, a esta cade de texto se le conoce como `docstring` y esta delimitado por triples `""" aqui el texto """`.
```python
def suma(a,b)
    """
    funcion para realizar la suma de dos numeros
    """
## Los docstring tambien nos permite explicar los poarametros que recibe y los datos de salida.
def resta(a,b)
    """
    a=a un numero entero.
    b= un numero entero.
    en ambos casos a,b no deben recibir valores menores 0.
    restornara un dato entero <int> positivo.
    """
    return a-b
```
> [!WARNING] En el proceso de documentacion tener encuenta de incluir a lo menos lo siguiente: 
1. Breve explicacin sobre que hace la funcion.
2. Especificar y caracteristicas de los parametros incluyendo sus tipos.
3. Restricciones de la funcion.
4. El valor que retorna y sus caracteristicas.

## Type-hints (Anotaciones de tipo)
Nos permite indicar que tipo de datos tendra una variable, parametros y el valor de retorno de una funcion.
Para utilizarlos debemos indicar el tipo de dato despue del reparador `:` , en el caso del valor de retorno usaremos `->` luego el tipo de dato y finalmente el separador `:` que indica el inicio del bloque de codigo de la funcion.
Las `anotaciones de tipo` son una herramienta que nos permite complementar la documentacion de nuestro codigo.
**Tenemos lo siguiente**
- **Simples**
    - int -> Numeros enteros.
    - float -> Numeros decimales.
    - bool -> Datos boleanos (verdad o falso).
    - str -> Datos de tipo texto o cadena.
    - list -> Lista `[]`.
    - tuple -> Tuplas `()`.
    - dict -> Diccionarios `{}`
- **Conpuestos**
Existen caso en los que necesitamos mas expresividad en la *anotacion de tipos* ¿Que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*?.
    - list[str] -> lista de cadenas de texto.
    - list[int] -> lista de numeros enteros.
    - dict{str,float} -> diccionariodonde las claves son cadenas de texto y los valores son flotantes/decimales.
- **Multiples** 
En el caso que queremos indicar que un determinado parametro puedeser de `tipo o de otro` tenemos que especificarlo usando el operador `|`.
- tuple|dict -> puede ser dato de tipo tupla o diccionario .
- list[str|int] -> lista cuyos elementos puede ser cadena de texto o ineteros.
- dict[str|int,float|int] -> 


